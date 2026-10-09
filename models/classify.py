"""Run a frozen block classifier on a page.

    from classify import load, classify
    clf = load("gbm")                       # "gbm", "logreg" or "seq" (models/frozen/<name>)
    result = classify(html, url, clf)       # blocks with probability and keep/drop, plus the kept text

    python models/classify.py gbm page.html [url]   # prints the kept main-content text

The model files are verified against the sha256 recorded in models/frozen/<name>/meta.json before use.
"""
import hashlib
import json
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import blocking as B  # noqa: E402
import features as F  # noqa: E402

FROZEN = HERE / "frozen"


def load(name: str) -> dict:
    d = FROZEN / name
    meta = json.loads((d / "meta.json").read_text())
    for f, h in meta["files_sha256"].items():
        if hashlib.sha256((d / f).read_bytes()).hexdigest() != h:
            raise RuntimeError(f"{d / f} does not match its frozen sha256")
    if meta["features"] != F.FEATURES:
        raise RuntimeError("features.py no longer matches the frozen feature list")
    if name == "seq":
        import torch
        import train as T
        ck = torch.load(d / "model.pt", weights_only=False)
        net = T.make_net(ck["n_in"], ck["n_tag"], ck["n_kind"])
        net.load_state_dict(ck["state_dict"])
        net.eval()
        model = (net, ck["mu"], ck["sd"])
    else:
        import joblib
        model = joblib.load(d / "model.joblib")
    return {"name": name, "model": model, "threshold": meta["threshold"], "meta": meta}


def predict_proba(clf: dict, X) -> np.ndarray:
    if not len(X):
        return np.zeros(0)
    if clf["name"] != "seq":
        return clf["model"].predict_proba(X[F.FEATURES])[:, 1]
    import torch
    import train as T
    net, mu, sd = clf["model"]
    num = X[F.NUMERIC].to_numpy(np.float32)
    Xs = np.clip((num - mu) / sd, -T.GRU["clip"], T.GRU["clip"]).astype(np.float32)
    with torch.no_grad():
        return T.seq_predict(net, [(0, len(Xs))], Xs, X.tag_code.to_numpy(np.int64), X.kind_code.to_numpy(np.int64))


def classify(html: str, url: str, clf: dict) -> dict:
    """Segment the page, featurize, score every block; keep blocks with probability >= the frozen threshold."""
    _, blocks = B.segment(html)
    X = F.page_features(blocks, F.trafilatura_text(html, url))
    p = predict_proba(clf, X)
    keep = p >= clf["threshold"]
    return {"blocks": [{"index": b.index, "tag": str(b.tag), "kind": b.kind, "text": b.text, "prob": float(pr),
                        "main_content": bool(k)} for b, pr, k in zip(blocks, p, keep)],
            "text": "\n\n".join(b.text for b, k in zip(blocks, keep) if k)}


if __name__ == "__main__":
    name, path = sys.argv[1], sys.argv[2]
    url = sys.argv[3] if len(sys.argv) > 3 else None
    print(classify(pathlib.Path(path).read_text(encoding="utf-8", errors="replace"), url, load(name))["text"])
