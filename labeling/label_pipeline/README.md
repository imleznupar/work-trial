# Labeling pipeline

This package discovers webpages, saves HTML snapshots, splits them into text
blocks, and labels each block as `content`, `boilerplate`, or `uncertain`.
Failed labeling batches are marked `unresolved`. The labels can then be used
to produce extraction references and evaluation questions, or evaluated
against the WCXB dev benchmark.

The main flow is:

```text
Candidate URLs → HTML snapshots → text blocks → model labels
                                               ├→ dataset summary
                                               ├→ reference Markdown and questions
                                               └→ WCXB dev evaluation
```

## What each script does

### `__main__.py` — general command-line interface

Runs with `python -m labeling`. Provides five commands:

- `discover`: selects URLs from manual JSONL, a URL dataset, or seed sitemaps,
  and writes candidate metadata plus a discovery report.
- `fetch`: downloads candidates into saved HTML snapshots and updates their
  metadata with fetch results.
- `label`: labels saved snapshots and writes page envelopes containing all
  block labels. Existing results are retained and successful batches cached.
- `evaluate`: evaluates saved labels against WCXB dev annotations.
- `run`: labels WCXB dev snapshots and then evaluates the results.

The WCXB path uses existing snapshots and supports only the dev split.

### `generate_balanced.py` — build a balanced labeled dataset

Reads CSV or JSONL candidates with `url` and `page_type`, fetches HTML, and
labels pages concurrently. Defaults to 20 pages per type across article,
documentation, forum, product, listing, collection, and service pages, with
at most three pages per domain.

Writes `pages.jsonl`, `labels.jsonl`, `fetch_attempts.jsonl`, `status.json`,
`snapshots/`, and `cache/` under the output directory. Reruns resume saved
work and retry missing or unresolved labels. Options control worker count,
batch sizes, quotas, fetch retries, and minimum labeled content size.

For a test split, it excludes dev URLs, redirect destinations, and identical
snapshots. Additional exclusion files can be supplied with `--exclude`.
Shared domains are recorded but allowed. WCXB dev URLs are excluded when
benchmark metadata is available.

### `discovery.py` — URL discovery and HTML fetching helpers

Normalizes URLs, removes common tracking parameters, assigns page types,
and selects candidates from supplied files or seed-site sitemaps. General
discovery records benchmark URL/domain overlap rather than excluding it.

Its `PoliteHTTP` client checks robots.txt, respects crawl delays, checks
redirect destinations, and limits response size. Fetching saves UTF-8 HTML
under a content hash and records status, timestamps, redirects, and errors.
Called by the general CLI and balanced generator.

### `segmentation.py` — split HTML into stable text blocks

Parses and cleans HTML, then emits blocks in DOM order: paragraphs, headings,
list items, tables, code, quotes, captions, terms, and text containers.
Tables and code blocks are kept whole; other blocks use their own inline
text so nested structural content is not counted twice.

This module defines the block boundaries used by labeling and annotations.
Changing it changes segmentation provenance and can invalidate saved labels.

### `page_features.py` — describe block structure

Computes ancestor information, link counts/link density, and visibility
signals such as `display:none`, `aria-hidden`, and screen-reader classes.
These HTML features are included in the block records sent to the model.
It does not assign content labels itself.

### `llm.py` — model labeling, validation, and cache

Creates stable block IDs and sends batches of blocks, with nearby context,
to an OpenAI or Gemini model. The prompt distinguishes primary content from
boilerplate and allows uncertain labels.

Validates block IDs, label values, confidence, and response completeness.
Caches successful batches, records model provenance and token usage, and
retries failures. Failed batches and individual blocks that exceed the
configured prompt budget remain unresolved. `label_page()` returns the
page metadata and its full labeled block records.

### `split_guard.py` — prevent dataset overlap

Loads excluded page metadata or label envelopes and collects their URLs,
redirect destinations, snapshot hashes, and domains. Rejects matching URLs
or exact snapshots when selecting another split. Tracks domain overlap
without rejecting it.

### `summarize_generated.py` — validate and summarize labels

Reads a generated dataset's `labels.jsonl` and optional `status.json`.
Checks duplicate page IDs, snapshot hashes, benchmark URL exclusion, and
dev overlap for a test split.

Writes `blocks.jsonl` with one row per block, `inventory.csv` with page URLs
and label counts, and `summary.json`/`report.md` with totals and completion
status. Completion requires the requested page quota for every type and no
unresolved labels. Uncertain labels remain abstentions.

### `page_annotations.py` — extraction references and grounded questions

Reads saved labels and their HTML snapshots. Renders content-labeled blocks
into reference Markdown while preserving headings, links, lists, tables,
and code. Derives must-include/must-exclude snippets and structure counts.

Uses Gemini to generate evaluation questions with expected answers, grading
points, and quoted block evidence. Validates that evidence quotes occur in
the source blocks and reuses successful questions on reruns.

Writes `golden_markdown/`, `annotations.jsonl`, `annotations_summary.json`,
and `qa_cache/`. These references are derived from model labels, rather than
human gold annotations.

### `evaluation.py` — score against WCXB dev ground truth

Reads WCXB dev labels, checks snapshot and segmentation identity, and aligns
blocks to the benchmark reference content. Calculates block-level and
character-weighted precision, recall, agreement, and coverage. Also renders
selected content into Markdown and scores extraction quality.

Writes aggregate and per-page reports, aligned blocks, disagreement examples,
and extracted Markdown. Compares available baseline outputs. This module
depends on the external benchmark project's evaluation modules and supports
only WCXB dev, not the newly discovered test dataset.

### `common.py` — shared paths and file utilities

Defines workspace and external project paths, SHA-256 hashing, UTC timestamps,
JSON/JSONL reading, and atomic output writes. Loads WCXB dev page metadata
without reading its ground-truth annotations.

`LABELING_PROJECT_ROOT` overrides the external project root, which defaults
to this workspace's parent directory. Pipeline outputs default to this
workspace's `data/` and `results/` directories.

### `__init__.py` — package marker

Marks `labeling` as a Python package. Contains a descriptive docstring and
no executable pipeline logic.

## Setup and usage

Run commands from the workspace root with Python 3.10+ and these dependencies:

```sh
python -m pip install requests lxml
```

For block labeling, set `LABELING_PROVIDER` to `openai` (default) or `gemini`
and supply `OPENAI_API_KEY` or `GEMINI_API_KEY`. `LABELING_API_KEY` can override
the provider-specific key. `LABELING_MODEL` overrides the default model;
`LABELING_BASE_URL` overrides the OpenAI-compatible endpoint.

Page-level QA generation uses Gemini independently of `LABELING_PROVIDER`,
requires `LABELING_API_KEY` or `GEMINI_API_KEY`, and accepts `--model`.
Model calls incur API charges.

Build and summarize a discovered dev dataset:

```sh
python -m labeling.generate_balanced --candidates candidates.csv --output data/dev --per-type 20
python -m labeling.summarize_generated --input data/dev
```

Build a separate test dataset and derive annotations:

```sh
python -m labeling.generate_balanced --candidates test_candidates.jsonl --split test --output data/test --per-type 20
python -m labeling.summarize_generated --input data/test
python -m labeling.page_annotations --input data/test
```

Test generation requires existing `data/dev/pages.jsonl` metadata. Balanced
generation with explicit candidates can run without the external benchmark
project; general discovery and WCXB evaluation require that project.

With the external benchmark project configured, label and evaluate WCXB dev:

```sh
python -m labeling run --dataset wcxb
```

Each command-line module supports `--help` for its options.
