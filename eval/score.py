"""Score the saved outputs on the 210 test pages and write eval/results/REPORT.md + scores.csv.

Per (system, page):
  golden word P/R/F1  bag-of-words overlap of the output text with the golden markdown text (WCXB-style word F1)
  include             share of must_include snippets present (markdown -> text, case-folded Unicode alphanumerics)
  exclude             share of must_exclude snippets absent (1 - leak); pages with no exclusion snippets skipped
  structure           mean over structure types the golden page has (headings, tables, list items, code) of
                      min(observed / expected, 1)
  QA evidence proxy   share of the page's QAs whose evidence quotes all appear in the output (deterministic)
  QA (model)          from eval/results/qa_results.csv when available: share graded CORRECT; NOT_FOUND / INCORRECT
  tokens              cl100k_base tokens of the output
  runtime             per page: CPU wall ms (classifiers, trafilatura; one process, sequential, single thread) or
                      GPU ms on an L4 (Pulpie, batch 1, after warm-up)
Block level (classifiers, and trafilatura via "block text appears in trafilatura's output"): P/R/F1 and
char-weighted P/R/F1 against the reference block labels (uncertain blocks excluded).
Paired page bootstrap (10,000 resamples, seed 0) of each system minus trafilatura.
"""
import csv
import json
import math

import numpy as np
import pandas as pd
import tiktoken

import common as E

ENC = tiktoken.get_encoding("cl100k_base")
SEED, NBOOT = 0, 10_000


def page_rows():
    anns = {a["page_id"]: a for a in E.annotations()}
    rows = []
    for s in E.SYSTEMS:
        runs = {r["page_id"]: r for r in map(json.loads, open(E.OUT / "_runs" / f"{s}.jsonl"))}
        for p in E.pages():
            a = anns[p["page_id"]]
            md = (E.OUT / s / f"{p['page_id']}.md").read_text(encoding="utf-8")
            text = E.md_to_text(md)
            key = E.alnum_key(text)
            P, R, F1 = E.word_prf(text, E.md_to_text(a["golden_markdown"]))
            inc = np.mean([E.snippet_in(x, key) for x in a["must_include"]]) if a["must_include"] else np.nan
            exc = np.mean([not E.snippet_in(x, key) for x in a["must_exclude"]]) if a["must_exclude"] else np.nan
            st, _, _ = E.structure_score(a["structure_checks"], md)
            qa_ev = np.mean([all(E.snippet_in(ev["quote"], key) for ev in q["evidence"]) for q in a["qa_questions"]])
            r = runs[p["page_id"]]
            rows.append({"system": s, "page_id": p["page_id"], "page_type": p["page_type"], "word_P": P, "word_R": R,
                         "word_F1": F1, "include": inc, "exclude": exc,
                         "structure": np.nan if st is None else st, "qa_evidence": qa_ev,
                         "tokens": len(ENC.encode(md, disallowed_special=())),
                         "runtime_ms": r.get("wall_ms", r.get("gpu_ms")), "cpu_ms": r.get("cpu_ms"),
                         "empty": r["empty"], "error": bool(r["error"])})
    return pd.DataFrame(rows)


def qa_rows():
    path = E.RESULTS / "qa_results.csv"
    if not path.exists():
        return None
    q = pd.read_csv(path, dtype={"page_id": str})
    if (q.verdict == "API_ERROR").all():
        return None
    return q


def block_rows():
    """Reference labels joined to each classifier's decisions; trafilatura via text presence in its output."""
    import labels as L
    ref = {}
    for line in open(E.TEST / "blocks.jsonl"):
        b = json.loads(line)
        lab = {"content": 1, "boilerplate": 0}.get(b.get("label")) if b.get("status", "resolved") == "resolved" else None
        ref[(b["page_id"], b["block_index"])] = (lab, len(b["text"]), b["text"], b["page_type"])
    out = []
    for s in ("gbm", "logreg", "seq"):
        for pg in map(json.loads, open(E.OUT / "_blocks" / f"{s}.jsonl")):
            for b in pg["blocks"]:
                lab, n, _, t = ref[(pg["page_id"], b["block_index"])]
                if lab is not None:
                    out.append({"system": s, "page_id": pg["page_id"], "page_type": t, "y": lab, "pred": b["keep"], "chars": n})
    by_page = {}
    for (pid, i), v in ref.items():
        by_page.setdefault(pid, []).append((i, v))
    for pid, bl in by_page.items():
        tr = L.fuzzy_norm(E.md_to_text((E.OUT / "trafilatura" / f"{pid}.md").read_text(encoding="utf-8")))
        for i, (lab, n, text, t) in bl:
            if lab is not None:
                out.append({"system": "trafilatura", "page_id": pid, "page_type": t, "y": lab, "chars": n,
                            "pred": L.presence(L.fuzzy_norm(text), tr) >= L.DUP_THRESHOLD})
    return pd.DataFrame(out)


def prf(y, pred, w):
    tp, fp, fn = (float(np.sum(w * m)) for m in (pred & (y == 1), pred & (y == 0), ~pred & (y == 1)))
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    return p, r, (2 * p * r / (p + r) if p + r else 0.0)


def boot(a, b, seed=SEED, n=NBOOT):
    m = ~(np.isnan(a) | np.isnan(b))
    d = (b - a)[m]
    rng = np.random.RandomState(seed)
    idx = rng.randint(0, len(d), (n, len(d)))
    ds = d[idx].mean(1)
    return d.mean(), np.percentile(ds, 2.5), np.percentile(ds, 97.5)


def fmt_ci(t, nd=3):
    return f"{t[0]:+.{nd}f} [{t[1]:+.{nd}f}, {t[2]:+.{nd}f}]"


def table(head, rows):
    return ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(map(str, r)) + " |" for r in rows]


def main():
    E.RESULTS.mkdir(parents=True, exist_ok=True)
    df = page_rows()
    qa = qa_rows()
    if qa is not None:
        acc = qa.assign(c=(qa.verdict == "CORRECT").astype(float)).groupby(["system", "page_id"]).c.mean()
        df["qa_model"] = [acc.get((s, p), np.nan) for s, p in zip(df.system, df.page_id)]
    df.to_csv(E.RESULTS / "scores.csv", index=False)
    blk = block_rows()
    pulpie = json.load(open(E.OUT / "_runs/pulpie_final_summary.json"))
    T = {s: df[df.system == s].set_index("page_id") for s in E.SYSTEMS}

    L = ["# Final evaluation on the test split (210 pages)", "",
         f"Test pages: `{E.TEST.relative_to(E.ROOT)}` (30 per type: article, collection, documentation, forum, listing, "
         "product, service). References (golden markdown, snippets, structure counts, QAs) are model-generated from "
         "Gemini block labels, not independent human gold. No training URL or snapshot overlap, but 207 of 210 pages share "
         "a domain with the training pages, so this measures new pages on mostly familiar domains.", "",
         "Systems: the three frozen block classifiers (`models/frozen/`, kept blocks rendered to markdown), trafilatura "
         "(markdown, tables, links) and Pulpie (0.0.2, orange-small) on a Modal L4 GPU. Outputs: `eval/outputs/`. "
         "Errors and empty outputs count as empty.", ""]
    qa_note = ("model-based QA accuracy (gemini-3.8-flash answers from the output only; separate grader against the "
               "expected answer and required points)" if qa is not None else
               "**model-based QA: not run** (the Gemini API returned 402 \"prepayment credits depleted\" on every call; "
               "`eval/qa.py` is ready to rerun and this report picks the results up automatically)")
    L += ["## Summary", "", f"Means over pages. QA: {qa_note}. QA evidence proxy = all evidence quotes of a question "
          "appear in the output.", ""]
    cols = [("word_F1", "golden word F1 ↑"), ("word_P", "word P"), ("word_R", "word R"), ("include", "include ↑"),
            ("exclude", "exclude ↑"), ("structure", "structure ↑"), ("qa_evidence", "QA evidence proxy ↑")]
    if qa is not None:
        cols.append(("qa_model", "QA (model) ↑"))
    rows = []
    for s in E.SYSTEMS:
        g = T[s]
        rt = (f"{g.runtime_ms.mean():.0f} / {g.runtime_ms.median():.0f} ms "
              + ("GPU (L4)" if s == "pulpie" else "CPU"))
        rows.append([f"**{E.LABELS[s]}**"] + [f"{g[c].mean():.3f}" for c, _ in cols]
                    + [f"{g.tokens.mean():,.0f}", rt, f"{int(g["empty"].sum())} / {int(g["error"].sum())}"])
    L += table(["system"] + [h for _, h in cols] + ["tokens", "runtime / page (mean / median)", "empty / errors"], rows)

    if qa is not None:
        L += ["", "## Model-based QA detail", ""]
        rows = []
        for s in E.SYSTEMS:
            q = qa[qa.system == s]
            hard = q[q.difficulty == "hard"]
            rows.append([E.LABELS[s], f"{(q.verdict == 'CORRECT').mean():.3f}", f"{(hard.verdict == 'CORRECT').mean():.3f}",
                         f"{(q.verdict == 'NOT_FOUND').mean():.3f}", f"{(q.verdict == 'INCORRECT').mean():.3f}",
                         int((q.verdict == "API_ERROR").sum())])
        L += table(["system", "accuracy (all 673)", "accuracy (hard 256)", "NOT_FOUND", "INCORRECT", "API errors"], rows)
        u = json.load(open(E.RESULTS / "qa_usage.json"))
        L += ["", f"QA cost: {u['answers']['calls'] + u['grades']['calls']:,} calls, "
              f"{u['answers']['in'] + u['grades']['in']:,} input tokens, ${u['total_usd']:.2f}."]

    L += ["", "## Paired differences vs trafilatura (page bootstrap, 10,000 resamples, 95% CI)", ""]
    mets = [c for c, _ in cols if c not in ("word_P", "word_R")]
    rows = []
    for s in E.SYSTEMS:
        if s == "trafilatura":
            continue
        rows.append([E.LABELS[s]] + [fmt_ci(boot(T["trafilatura"][m].to_numpy(float), T[s][m].loc[T["trafilatura"].index].to_numpy(float)))
                                     for m in mets])
    L += table(["system"] + [dict(cols)[m] for m in mets], rows)

    L += ["", "## Block level vs the reference block labels", "",
          "Pulpie is not block-based, so it has no row here. trafilatura: a block counts as kept if its text appears in "
          "trafilatura's output.", ""]
    rows = []
    for s in ("gbm", "logreg", "seq", "trafilatura"):
        b = blk[blk.system == s]
        y, pr, w = b.y.to_numpy(), b.pred.to_numpy(bool), b.chars.to_numpy(float)
        bp, br, bf = prf(y, pr, np.ones(len(y)))
        cp, cr, cf = prf(y, pr, w)
        rows.append([E.LABELS[s], f"{bp:.3f} / {br:.3f} / {bf:.4f}", f"{cp:.3f} / {cr:.3f} / **{cf:.4f}**"])
    L += table(["system", "block P / R / F1", "char P / R / F1"], rows)

    types = ["article", "collection", "documentation", "forum", "listing", "product", "service"]
    for m, title in (("word_F1", "golden word F1"), ("include", "include"), ("exclude", "exclude"),
                     ("structure", "structure"), ("qa_evidence", "QA evidence proxy")) + ((("qa_model", "QA (model)"),) if qa is not None else ()):
        L += ["", f"## By page type: {title}", ""]
        L += table(["system"] + types, [[E.LABELS[s]] + [f"{T[s][T[s].page_type == t][m].mean():.3f}" for t in types]
                                        for s in E.SYSTEMS])
    L += ["", "## By page type: block-level char F1", ""]
    rows = []
    for s in ("gbm", "logreg", "seq", "trafilatura"):
        b = blk[blk.system == s]
        rows.append([E.LABELS[s]] + [f"{prf(b[b.page_type == t].y.to_numpy(), b[b.page_type == t].pred.to_numpy(bool), b[b.page_type == t].chars.to_numpy(float))[2]:.3f}" for t in types])
    L += table(["system"] + types, rows)

    # runtime and cost
    cpu = {s: T[s].runtime_ms for s in ("gbm", "logreg", "seq", "trafilatura")}
    L += ["", "## Runtime", "",
          "CPU systems: Apple-silicon laptop CPU, one process, pages sequential, single-threaded inference, after a "
          "warm-up page; time covers raw HTML to markdown (classifiers include segmentation, their own trafilatura run "
          "for the agreement features, features, inference and rendering). Pulpie: per-page GPU time on one Modal L4 "
          "(batch size 1, cuda-synchronized, after warm-up).", ""]
    rows = []
    for s in E.SYSTEMS:
        r = T[s].runtime_ms
        thr = 1000 / r.mean()
        rows.append([E.LABELS[s], "GPU L4" if s == "pulpie" else "CPU (1 core)", f"{r.mean():.0f}", f"{r.median():.0f}",
                     f"{r.quantile(0.95):.0f}", f"{thr:.1f}"])
    L += table(["system", "hardware", "mean ms", "median ms", "p95 ms", "pages / s"], rows)
    cpu_core_s, l4_s = 0.0000131, pulpie["usd_per_s"]
    L += ["", f"Pulpie run: model load {pulpie['model_load_s']:.1f} s, container startup {pulpie['container_startup_s']:.1f} s, "
          f"{pulpie['containers']} container(s), billed GPU time ≈ {pulpie['billed_gpu_s_estimate']:.0f} s "
          f"(≈ ${pulpie['billed_gpu_usd_estimate']:.3f}).", "",
          f"Projected compute cost per 1 million pages at the measured throughput (Modal list prices: L4 ${l4_s}/s, "
          f"CPU ${cpu_core_s}/core/s; memory and orchestration excluded, no batching or parallelism assumed):", ""]
    rows = []
    for s in E.SYSTEMS:
        sec = T[s].runtime_ms.mean() / 1000
        price = l4_s if s == "pulpie" else cpu_core_s
        rows.append([E.LABELS[s], f"{sec * 1e6 / 3600:,.0f} {'GPU' if s == 'pulpie' else 'core'}-hours",
                     f"${sec * 1e6 * price:,.2f}"])
    L += table(["system", "compute per 1M pages", "cost per 1M pages"], rows)
    L += ["", "## Notes", "",
          "- One must_include snippet cannot be matched even in the golden markdown under this normalization "
          "(1,212 / 1,213), so the ceiling for include is just under 1.",
          f"- Empty outputs: {', '.join(f'{E.LABELS[s]} {int(T[s]["empty"].sum())}' for s in E.SYSTEMS)} (scored as empty).",
          "- The BiGRU's frozen threshold (0.69) is the highest of the three, which is why it returns empty output on "
          "some pages.",
          "- References are model-generated; scores measure agreement with that reference, not human judgment.",
          "- **Reference bias in favor of the three classifiers:** the test references come from the same Gemini "
          "block-labeling pipeline (same rubric, same segmentation as `models/blocking.py`) that produced the 140 "
          "labeled training pages, and 207 of 210 test pages share a domain with training pages. trafilatura and "
          "Pulpie were never trained on this labeler, so their gap is partly a label-convention gap. The classifier vs "
          "classifier comparison is fair; the classifier vs trafilatura/Pulpie margin is an upper bound."]
    (E.RESULTS / "REPORT.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[:40]))


if __name__ == "__main__":
    main()
