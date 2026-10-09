# models

Three block classifiers that label each HTML block as **main content** or **noise**. All three share one
preprocessing step (HTML → blocks), one label set and one feature table.

## Files

| file | purpose |
|---|---|
| `blocking.py` | Segment raw HTML into blocks (text elements by their own inline content; tables/`pre` whole; other elements only with ≥ 20 chars of direct text). Matches the labeling segmentation block-for-block. |
| `labels.py` | Block labels. WCXB dev: block text aligned to the page's ground-truth `main_content` (fuzzy match + short-block guard). Labeled pages: LLM labels (content = 1, boilerplate = 0, uncertain excluded). |
| `features.py` | 57 per-block features from the HTML and trafilatura only: text stats, link density, tag/kind, depth and position, sibling repetition, ancestor and class/id signals, boilerplate phrases, trafilatura agreement. |
| `build_dataset.py` | Runs blocking → labels → features over both sources → `data/dataset/` (356k blocks, 1,611 pages). |
| `train.py` | 5-fold CV grouped by domain, threshold chosen on held-out predictions, final fit on all data, frozen to `frozen/`. |
| `classify.py` | Load a frozen model (sha256-verified) and classify a page's blocks. |

## Data

- `data/wcxb/`: WCXB dev split only (sparse clone of `github.com/Murrough-Foley/web-content-extraction-benchmark`, commit `c039d5e`). The test split is never downloaded.
- 140 LLM-labeled pages from the labeling project's `data/dev`.
- `data/dataset/`: the built block table and build report. `data/cv/`: out-of-fold predictions and CV results.

## Frozen models

`frozen/{gbm,logreg,seq}/` each holds the model file and a `meta.json` with features, threshold, CV metrics,
training-data hashes, code hashes, package versions and the model file's sha256. Files are read-only.
