# eval

Final evaluation on the 210-page test split (`labeling/data/test`, 30 pages per type) of five systems: the three
frozen block classifiers (`gbm`, `logreg`, `seq`), trafilatura, and Pulpie on a Modal L4 GPU. The report is in
`results/REPORT.md`.

## Pipeline

```bash
cd eval
../.venv/bin/python run_cpu.py                          # gbm, logreg, seq, trafilatura outputs + CPU runtime
../.venv/bin/modal run pulpie_modal.py --mode check     # 3-page GPU vs local CPU equality check
../.venv/bin/modal run pulpie_modal.py --mode final     # Pulpie on all 210 pages + GPU runtime
../.venv/bin/python qa.py                               # model-based QA (needs GEMINI_API_KEY)
../.venv/bin/python score.py                            # metrics + results/REPORT.md
```

## Files

| file | purpose |
|---|---|
| `common.py` | Test-data paths, markdown → text, snippet normalization (case-folded alphanumerics), word F1, markdown structure counts. |
| `run_cpu.py` | Runs the classifiers (kept blocks rendered to markdown) and trafilatura; times each page from raw HTML to markdown (one process, single thread, after warm-up). |
| `pulpie_modal.py` | Self-contained Modal app: pulpie 0.0.2 / orange-small (pinned revision, html2text included) on one L4; per-page GPU latency, startup, throughput, cost. |
| `qa.py` | Gemini 3.8 Flash answers each QA from one system's markdown only; a separate grader (never sees the system name) marks CORRECT / INCORRECT / NOT_FOUND against the expected answer and required points. Cached, with timeouts and error logging. |
| `score.py` | Golden-markdown word F1, include / exclude snippet rates, structure, QA (model-based and evidence proxy), tokens, runtime, block-level char F1 vs the reference labels, per-type tables, paired bootstrap CIs vs trafilatura, cost per 1M pages. |

## Outputs

- `outputs/{system}/{page_id}.md`: each system's markdown.
- `outputs/_runs/`: per-page runtime, errors, and the Pulpie run summary.
- `outputs/_blocks/`: per-block probabilities and decisions for the classifiers.
- `results/`: `REPORT.md`, `scores.csv`, QA results, usage and error logs.

