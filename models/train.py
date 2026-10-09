"""Train, cross-validate and freeze the three block classifiers on the shared block table
(models/data/dataset/blocks.pkl.gz: WCXB dev + the 140 LLM-labeled pages).

Models (same features, models/features.py):
  gbm     HistGradientBoostingClassifier, balanced class weights, tag/kind as native categoricals
  logreg  LogisticRegression (L2, balanced class weights); standardized numerics, one-hot tag/kind;
          C chosen by an inner 3-fold domain-grouped CV on each training fold
  seq     sequence model: 2-layer bidirectional GRU (hidden 64) over each page's blocks in DOM order; standardized
          features + learned tag/kind embeddings; per-block sigmoid; class-weighted BCE; pages split into windows
          of 256 blocks with 32 overlap (overlapping predictions averaged); early stopping on a 10% domain-grouped
          validation split of the training data, max 20 epochs, seed 0. Unlabeled blocks are inputs but not targets.

Protocol:
  - 5 folds grouped by registrable domain over both sources (no domain in two folds).
  - Out-of-fold evaluation uses, for each held-out fold, the threshold maximizing pooled char F1 on the other four
    folds' out-of-fold predictions. The frozen operating threshold is the char-F1 optimum on all out-of-fold
    predictions.
  - The frozen model is refit on all labeled blocks with the same settings (logreg: the most common inner-CV C;
    seq: same early-stopping procedure) and written to models/frozen/{name}/ with meta.json; files are made read-only.
Usage: python models/train.py {gbm|logreg|seq|all}
"""
import hashlib
import json
import os
import pathlib
import platform
import stat
import sys
import time

import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import GroupKFold

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import features as F  # noqa: E402

DATA = HERE / "data/dataset"
CV = HERE / "data/cv"
FROZEN = HERE / "frozen"
THRESHOLDS = np.round(np.arange(0.05, 0.96, 0.01), 2)
SEED = 0
GBM_PARAMS = dict(max_iter=300, learning_rate=0.1, max_leaf_nodes=31, min_samples_leaf=40, l2_regularization=0.0,
                  early_stopping=False, class_weight="balanced", random_state=SEED,
                  categorical_features=F.CATEGORICAL)
LR_CS = [1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0]
GRU = dict(hidden=64, layers=2, tag_emb=8, kind_emb=4, window=256, overlap=32, batch=16, lr=2e-3, max_epochs=20,
           patience=3, val_share=0.1, clip=10.0)


# ---------------------------------------------------------------- data
def load():
    d = pd.read_pickle(DATA / "blocks.pkl.gz").sort_values(["page_id", "block_index"]).reset_index(drop=True)
    pages = d.groupby("page_id").domain.first()
    pf = dict(zip(pages.index, np.zeros(len(pages), dtype=int)))
    for k, (_, te) in enumerate(GroupKFold(n_splits=5).split(pages.index, groups=pages.to_numpy())):
        for i in te:
            pf[pages.index[i]] = k
    d["fold"] = d.page_id.map(pf).astype(int)
    d["labeled"] = d.label.notna()
    return d


# ---------------------------------------------------------------- metrics
def prf(y, pred, w=None):
    w = np.ones(len(y)) if w is None else w
    tp, fp, fn = (float(np.sum(w * m)) for m in (pred & (y == 1), pred & (y == 0), ~pred & (y == 1)))
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    return p, r, (2 * p * r / (p + r) if p + r else 0.0)


def bmetrics(y, pred, chars):
    bp, br, bf = prf(y, pred)
    cp, cr, cf = prf(y, pred, chars)
    return {"block_P": bp, "block_R": br, "block_F1": bf, "char_P": cp, "char_R": cr, "char_F1": cf, "n": int(len(y))}


def best_t(y, p, chars):
    return float(max((prf(y, p >= t, chars)[2], t) for t in THRESHOLDS)[1])


def evaluate(d, p):
    """Out-of-fold evaluation at per-fold thresholds (each chosen on the other folds)."""
    m = d.labeled.to_numpy()
    y = d.label.to_numpy(dtype=float)[m].astype(int)
    pr, c, fold = p[m], d.n_chars.to_numpy(float)[m], d.fold.to_numpy()[m]
    thr = [best_t(y[fold != k], pr[fold != k], c[fold != k]) for k in range(5)]
    pred = pr >= np.array(thr)[fold]
    per_fold = [bmetrics(y[fold == k], pred[fold == k], c[fold == k]) for k in range(5)]
    src, typ = d.source.to_numpy()[m], d.page_type.to_numpy()[m]
    out = {"per_fold_thresholds": thr, "frozen_threshold": best_t(y, pr, c),
           "pooled": bmetrics(y, pred, c), "per_fold": per_fold,
           "fold_mean": {k: float(np.mean([f[k] for f in per_fold])) for k in per_fold[0]},
           "fold_sd": {k: float(np.std([f[k] for f in per_fold], ddof=1)) for k in per_fold[0]},
           "by_source": {s: bmetrics(y[src == s], pred[src == s], c[src == s]) for s in sorted(set(src))},
           "by_source_type": {f"{s}/{t}": bmetrics(y[(src == s) & (typ == t)], pred[(src == s) & (typ == t)],
                                                  c[(src == s) & (typ == t)])
                              for s in sorted(set(src)) for t in sorted(set(typ[src == s]))}}
    return out, pred


# ---------------------------------------------------------------- GBM
def fit_gbm(X, y):
    from sklearn.ensemble import HistGradientBoostingClassifier
    return HistGradientBoostingClassifier(**GBM_PARAMS).fit(X, y)


# ---------------------------------------------------------------- logistic regression
def lr_pipeline(C):
    from sklearn.compose import ColumnTransformer
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    ct = ColumnTransformer([("num", StandardScaler(), F.NUMERIC),
                            ("cat", OneHotEncoder(handle_unknown="ignore"), F.CATEGORICAL)])
    return make_pipeline(ct, LogisticRegression(C=C, class_weight="balanced", max_iter=5000))


def _inner(args):
    C, X, y, c, g = args
    p = np.zeros(len(y))
    for tr, te in GroupKFold(n_splits=3).split(X, y, g):
        p[te] = lr_pipeline(C).fit(X.iloc[tr], y[tr]).predict_proba(X.iloc[te])[:, 1]
    t = best_t(y, p, c)
    return C, prf(y, p >= t, c)[2]


def choose_c(X, y, c, g):
    from multiprocessing import Pool
    with Pool(6) as pool:
        sc = pool.map(_inner, [(C, X, y, c, g) for C in LR_CS])
    return max(sc, key=lambda x: (x[1], -x[0]))[0], sc


# ---------------------------------------------------------------- sequence model (BiGRU)
def page_slices(d):
    pid = d.page_id.to_numpy()
    starts = np.r_[0, np.where(pid[1:] != pid[:-1])[0] + 1]
    return list(zip(starts, np.r_[starts[1:], len(pid)]))


def windows(s, e, W=GRU["window"], O=GRU["overlap"]):
    n = e - s
    if n <= W:
        return [(s, e)]
    out, st = [], 0
    while st + W < n:
        out.append((s + st, s + st + W))
        st += W - O
    out.append((e - W, e))
    return out


def make_net(n_in, n_tag, n_kind):
    import torch
    import torch.nn as nn

    class BiGRU(nn.Module):
        def __init__(self):
            super().__init__()
            self.tag = nn.Embedding(n_tag, GRU["tag_emb"])
            self.kind = nn.Embedding(n_kind, GRU["kind_emb"])
            self.gru = nn.GRU(n_in + GRU["tag_emb"] + GRU["kind_emb"], GRU["hidden"], num_layers=GRU["layers"],
                              bidirectional=True, batch_first=True)
            self.out = nn.Linear(2 * GRU["hidden"], 1)

        def forward(self, x, tag, kind):
            h, _ = self.gru(torch.cat([x, self.tag(tag), self.kind(kind)], -1))
            return self.out(h).squeeze(-1)
    return BiGRU()


def _batches(ws, B, rng=None):
    order = sorted(range(len(ws)), key=lambda i: ws[i][1] - ws[i][0])
    bs = [order[i:i + B] for i in range(0, len(order), B)]
    if rng is not None:
        rng.shuffle(bs)
    return bs


def _tensors(idx, ws, Xs, tag, kind, y=None, mask=None):
    import torch
    L = max(ws[i][1] - ws[i][0] for i in idx)
    x = np.zeros((len(idx), L, Xs.shape[1]), np.float32)
    t, k = np.zeros((len(idx), L), np.int64), np.zeros((len(idx), L), np.int64)
    m, yy = np.zeros((len(idx), L), np.float32), np.zeros((len(idx), L), np.float32)
    for j, i in enumerate(idx):
        s, e = ws[i]
        x[j, :e - s], t[j, :e - s], k[j, :e - s] = Xs[s:e], tag[s:e], kind[s:e]
        if y is not None:
            m[j, :e - s], yy[j, :e - s] = mask[s:e], y[s:e]
    return [torch.from_numpy(a) for a in (x, t, k, m, yy)]


def seq_inputs(d):
    return (d[F.NUMERIC].to_numpy(np.float32), d.tag_code.to_numpy(np.int64), d.kind_code.to_numpy(np.int64))


def seq_predict(net, slices, Xs, tag, kind):
    import torch
    net.eval()
    acc, cnt = np.zeros(len(Xs)), np.zeros(len(Xs))
    ws = [w for s, e in slices for w in windows(s, e)]
    with torch.no_grad():
        for idx in _batches(ws, 32):
            x, t, k, _, _ = _tensors(idx, ws, Xs, tag, kind)
            pr = torch.sigmoid(net(x, t, k)).numpy()
            for j, i in enumerate(idx):
                s, e = ws[i]
                acc[s:e] += pr[j, :e - s]
                cnt[s:e] += 1
    return acc / np.maximum(cnt, 1)


def fit_seq(d, train_pages, slices, n_tag, n_kind):
    """Train one BiGRU on the given page indices (early stopping on a 10% domain-grouped split of them)."""
    import torch
    from sklearn.model_selection import GroupShuffleSplit
    torch.manual_seed(SEED)
    rng = np.random.RandomState(SEED)
    page_dom = d.domain.to_numpy()[[s for s, _ in slices]]
    fit_i, val_i = next(GroupShuffleSplit(1, test_size=GRU["val_share"], random_state=SEED)
                        .split(train_pages, groups=page_dom[train_pages]))
    tr_blocks = np.concatenate([np.arange(*slices[p]) for p in train_pages])
    num, tag, kind = seq_inputs(d)
    mu, sd = num[tr_blocks].mean(0), num[tr_blocks].std(0) + 1e-6
    Xs = np.clip((num - mu) / sd, -GRU["clip"], GRU["clip"]).astype(np.float32)
    y = d.label.fillna(0).to_numpy(np.float32)
    mask = d.labeled.to_numpy(np.float32)
    fitw = [w for p in train_pages[fit_i] for w in windows(*slices[p])]
    valw = [w for p in train_pages[val_i] for w in windows(*slices[p])]
    lab = np.concatenate([np.arange(s, e) for s, e in fitw])
    yl = y[lab][mask[lab] > 0]
    pos_w = torch.tensor(float((yl == 0).sum() / max((yl == 1).sum(), 1)))
    net = make_net(Xs.shape[1], n_tag, n_kind)
    opt = torch.optim.Adam(net.parameters(), lr=GRU["lr"])

    def run(ws, train):
        net.train(train)
        tot = cnt = 0.0
        for idx in _batches(ws, GRU["batch"], rng if train else None):
            x, t, k, m, yy = _tensors(idx, ws, Xs, tag, kind, y, mask)
            if m.sum() == 0:
                continue
            with torch.set_grad_enabled(train):
                l = torch.nn.functional.binary_cross_entropy_with_logits(net(x, t, k), yy, pos_weight=pos_w,
                                                                         reduction="none")
                loss = (l * m).sum() / m.sum()
            if train:
                opt.zero_grad()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(net.parameters(), 1.0)
                opt.step()
            tot, cnt = tot + float((l * m).sum()), cnt + float(m.sum())
        return tot / max(cnt, 1)

    best, state, bad, hist = 1e9, None, 0, []
    for _ in range(GRU["max_epochs"]):
        hist.append((run(fitw, True), run(valw, False)))
        if hist[-1][1] < best - 1e-5:
            best, bad = hist[-1][1], 0
            state = {k: v.clone() for k, v in net.state_dict().items()}
        else:
            bad += 1
            if bad >= GRU["patience"]:
                break
    net.load_state_dict(state)
    return net, mu, sd, Xs, tag, kind, {"epochs": len(hist), "best_val_loss": best, "history": hist}


# ---------------------------------------------------------------- per-model CV + final fit
def cv_and_fit(name, d):
    import torch
    torch.set_num_threads(8)
    m = d.labeled.to_numpy()
    X, y = d[F.FEATURES], d.label.fillna(-1).to_numpy(int)
    c, g, fold = d.n_chars.to_numpy(float), d.domain.to_numpy(), d.fold.to_numpy()
    oof = np.full(len(d), np.nan)
    info = {"folds": []}
    if name == "seq":
        slices = page_slices(d)
        page_fold = fold[[s for s, _ in slices]]
        n_tag, n_kind = len(F.TAGS), len(F.KIND_CODE)
    for k in range(5):
        t0 = time.time()
        if name == "seq":
            net, mu, sd, Xs, tag, kind, h = fit_seq(d, np.where(page_fold != k)[0], slices, n_tag, n_kind)
            te_pages = np.where(page_fold == k)[0]
            p = seq_predict(net, [slices[i] for i in te_pages], Xs, tag, kind)
            te = np.concatenate([np.arange(*slices[i]) for i in te_pages])
            oof[te] = p[te]
            info["folds"].append({**h, "train_s": time.time() - t0})
        else:
            tr, te = np.where((fold != k) & m)[0], np.where(fold == k)[0]
            if name == "gbm":
                mod, extra = fit_gbm(X.iloc[tr], y[tr]), {}
            else:
                C, sc = choose_c(X.iloc[tr], y[tr], c[tr], g[tr])
                mod, extra = lr_pipeline(C).fit(X.iloc[tr], y[tr]), {"C": C, "inner_scores": sc}
            oof[te] = mod.predict_proba(X.iloc[te])[:, 1]
            info["folds"].append({**extra, "train_s": time.time() - t0})
        print(f"{name} fold {k}: {time.time() - t0:.0f}s", flush=True)
    CV.mkdir(parents=True, exist_ok=True)
    np.save(CV / f"{name}_oof.npy", oof)
    res, _ = evaluate(d, oof)
    res["train"] = info
    thr = res["frozen_threshold"]

    # final model on all labeled blocks
    t0 = time.time()
    out = FROZEN / name
    if out.exists():
        for f in out.iterdir():
            os.chmod(f, stat.S_IWUSR | stat.S_IRUSR)
    out.mkdir(parents=True, exist_ok=True)
    if name == "seq":
        net, mu, sd, *_, h = fit_seq(d, np.arange(len(slices)), slices, n_tag, n_kind)
        torch.save({"state_dict": net.state_dict(), "mu": mu, "sd": sd, "n_in": len(mu), "n_tag": n_tag,
                    "n_kind": n_kind, "config": GRU}, out / "model.pt")
        files, final = ["model.pt"], {"epochs": h["epochs"], "best_val_loss": h["best_val_loss"]}
    else:
        tr = np.where(m)[0]
        if name == "gbm":
            mod, final = fit_gbm(X.iloc[tr], y[tr]), {"params": {k: v for k, v in GBM_PARAMS.items()}}
        else:
            Cm = pd.Series([f["C"] for f in info["folds"]]).mode().iloc[0]
            mod, final = lr_pipeline(Cm).fit(X.iloc[tr], y[tr]), {"C": float(Cm)}
        joblib.dump(mod, out / "model.joblib")
        files = ["model.joblib"]
    final["train_s"] = time.time() - t0
    freeze(name, out, files, thr, res, final, d)
    (CV / f"{name}_results.json").write_text(json.dumps(res, indent=1, default=float))
    p = res["pooled"]
    print(f"[{name}] OOF char F1 {p['char_F1']:.4f} (folds {res['fold_mean']['char_F1']:.4f} ± "
          f"{res['fold_sd']['char_F1']:.4f}) block F1 {p['block_F1']:.4f} | frozen threshold {thr}", flush=True)
    return res


def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def freeze(name, out, files, thr, res, final, d):
    import sklearn
    import torch
    build = json.loads((DATA / "build_report.json").read_text())
    meta = {
        "model": name, "frozen_at": time.strftime("%Y-%m-%d %H:%M"), "threshold": thr,
        "threshold_rule": "maximizes pooled char-weighted F1 on all out-of-fold predictions (5 domain-grouped folds)",
        "features": F.FEATURES, "categorical": F.CATEGORICAL, "tags": F.TAGS,
        "training_data": {"sources": build["labeled_blocks"], "pages": build["pages_used"],
                          "wcxb_git_commit": build["wcxb_git_commit"], "labeling_sha256": build["labeling_sha256"],
                          "dataset_sha256": sha(DATA / "blocks.pkl.gz"),
                          "label_rules": "wcxb: block text vs ground-truth main_content (models/labels.py); "
                                         "labeling: LLM labels content=1 boilerplate=0, uncertain excluded"},
        "final_fit": final,
        "cv": {k: res[k] for k in ("pooled", "fold_mean", "fold_sd", "per_fold_thresholds", "by_source")},
        "code_sha256": {f: sha(HERE / f) for f in ("blocking.py", "labels.py", "features.py", "train.py")},
        "versions": {"python": platform.python_version(), "sklearn": sklearn.__version__, "torch": torch.__version__,
                     "numpy": np.__version__, "pandas": pd.__version__},
        "files_sha256": {f: sha(out / f) for f in files},
    }
    (out / "meta.json").write_text(json.dumps(meta, indent=1, default=float))
    for f in files + ["meta.json"]:
        os.chmod(out / f, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)  # read-only: frozen


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    d = load()
    print(f"{len(d):,} blocks, {d.labeled.sum():,} labeled, {d.page_id.nunique()} pages, {d.domain.nunique()} domains")
    for n in (["gbm", "logreg", "seq"] if which == "all" else [which]):
        cv_and_fit(n, d)
