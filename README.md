# HTML main-content extraction with block classifiers

Turn a raw web page into its main content for AI agents, dropping navigation, ads, footers and other boilerplate.
Each page is split into blocks (paragraphs, headings, list items, tables, ...), and a classifier decides for each
block whether it is **main content** or **noise**. Three classifiers are trained on the same blocks and features: a
gradient booster, a logistic regression and a BiGRU sequence model.

## Layout

| directory | contents |
|---|---|
| `labeling/` | LLM block-labeling pipeline (`label_pipeline/`) and its data: block labels for the 140 training pages (`data/dev`) and the 210-page test split with golden markdown, snippets, structure checks, QAs and reference block labels (`data/test`). |
| `models/` | Shared blocking, labels and features; dataset build; training with domain-grouped CV; the three frozen models (`models/frozen/`). See `models/README.md`. |
| `eval/` | Final evaluation of the three models, trafilatura and Pulpie (Modal L4 GPU) on the test split. See `eval/README.md`; results in `eval/results/REPORT.md`. |
| `demo/` | "Block lens": a local web app that shows every block of a page with each model's decision and probability. See `demo/README.md`. |

## Data

- **Training:** WCXB dev (1,497 pages, CC-BY-4.0; block labels derived from its ground-truth main content) plus the
  140 LLM-labeled pages.
- **Test:** 210 separately labeled pages, kept out of training and tuning. WCXB's own test split is never used.

## Quick start

All commands run from this directory with the existing environment (`.venv`).

```bash
.venv/bin/python demo/server.py                          # demo at http://127.0.0.1:8000
.venv/bin/python models/classify.py gbm page.html URL    # print a page's main content (gbm | logreg | seq)
.venv/bin/python models/build_dataset.py && .venv/bin/python models/train.py all   # rebuild + retrain + refreeze
cd eval && ../.venv/bin/python run_cpu.py && ../.venv/bin/python score.py           # re-run the CPU part of the eval
```

Pulpie on GPU needs Modal (`.venv/bin/modal token new`); model-based QA needs `GEMINI_API_KEY`.

## Notes

- Labels are proxies: WCXB block labels come from text alignment, and the other pages from Gemini, not human
  annotators.
- The test references come from the same labeling pipeline as part of the training data, which favors the three
  classifiers over trafilatura and Pulpie; see the caveats in `eval/results/REPORT.md`.
