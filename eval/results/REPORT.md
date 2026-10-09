# Final evaluation on the test split (210 pages)

Test pages: `labeling/data/test` (30 per type: article, collection, documentation, forum, listing, product, service). References (golden markdown, snippets, structure counts, QAs) are model-generated from Gemini block labels, not independent human gold. No training URL or snapshot overlap, but 207 of 210 pages share a domain with the training pages, so this measures new pages on mostly familiar domains.

Systems: the three frozen block classifiers (`models/frozen/`, kept blocks rendered to markdown), trafilatura (markdown, tables, links) and Pulpie (0.0.2, orange-small) on a Modal L4 GPU. Outputs: `eval/outputs/`. Errors and empty outputs count as empty.

## Summary

Means over pages. QA: **model-based QA: not run** (the Gemini API returned 402 "prepayment credits depleted" on every call; `eval/qa.py` is ready to rerun and this report picks the results up automatically). QA evidence proxy = all evidence quotes of a question appear in the output.

| system | golden word F1 ↑ | word P | word R | include ↑ | exclude ↑ | structure ↑ | QA evidence proxy ↑ | tokens | runtime / page (mean / median) | empty / errors |
|---|---|---|---|---|---|---|---|---|---|---|
| **Gradient booster** | 0.895 | 0.931 | 0.883 | 0.920 | 0.908 | 0.792 | 0.842 | 1,639 | 106 / 73 ms CPU | 0 / 0 |
| **Logistic regression** | 0.799 | 0.898 | 0.760 | 0.798 | 0.900 | 0.685 | 0.721 | 1,591 | 96 / 65 ms CPU | 0 / 0 |
| **Sequence model (BiGRU)** | 0.739 | 0.921 | 0.671 | 0.711 | 0.961 | 0.508 | 0.652 | 1,453 | 100 / 69 ms CPU | 7 / 0 |
| **trafilatura** | 0.675 | 0.879 | 0.608 | 0.639 | 0.912 | 0.308 | 0.558 | 1,573 | 62 / 35 ms CPU | 0 / 0 |
| **Pulpie (L4 GPU)** | 0.784 | 0.811 | 0.818 | 0.830 | 0.942 | 0.755 | 0.734 | 3,418 | 374 / 264 ms GPU (L4) | 0 / 0 |

## Paired differences vs trafilatura (page bootstrap, 10,000 resamples, 95% CI)

| system | golden word F1 ↑ | include ↑ | exclude ↑ | structure ↑ | QA evidence proxy ↑ |
|---|---|---|---|---|---|
| Gradient booster | +0.220 [+0.187, +0.255] | +0.281 [+0.237, +0.328] | -0.004 [-0.026, +0.018] | +0.484 [+0.428, +0.540] | +0.284 [+0.234, +0.335] |
| Logistic regression | +0.124 [+0.101, +0.147] | +0.160 [+0.125, +0.197] | -0.012 [-0.029, +0.003] | +0.377 [+0.321, +0.432] | +0.163 [+0.124, +0.204] |
| Sequence model (BiGRU) | +0.064 [+0.036, +0.093] | +0.072 [+0.033, +0.113] | +0.049 [+0.030, +0.069] | +0.200 [+0.147, +0.253] | +0.094 [+0.042, +0.146] |
| Pulpie (L4 GPU) | +0.109 [+0.078, +0.142] | +0.191 [+0.140, +0.242] | +0.030 [-0.002, +0.059] | +0.447 [+0.380, +0.513] | +0.176 [+0.110, +0.240] |

## Block level vs the reference block labels

Pulpie is not block-based, so it has no row here. trafilatura: a block counts as kept if its text appears in trafilatura's output.

| system | block P / R / F1 | char P / R / F1 |
|---|---|---|
| Gradient booster | 0.919 / 0.751 / 0.8268 | 0.967 / 0.863 / **0.9119** |
| Logistic regression | 0.912 / 0.648 / 0.7574 | 0.961 / 0.840 / **0.8965** |
| Sequence model (BiGRU) | 0.965 / 0.572 / 0.7180 | 0.986 / 0.791 / **0.8782** |
| trafilatura | 0.725 / 0.553 / 0.6276 | 0.940 / 0.692 / **0.7973** |

## By page type: golden word F1

| system | article | collection | documentation | forum | listing | product | service |
|---|---|---|---|---|---|---|---|
| Gradient booster | 0.881 | 0.862 | 0.925 | 0.896 | 0.882 | 0.870 | 0.947 |
| Logistic regression | 0.841 | 0.456 | 0.946 | 0.838 | 0.850 | 0.770 | 0.889 |
| Sequence model (BiGRU) | 0.780 | 0.322 | 0.922 | 0.802 | 0.776 | 0.672 | 0.898 |
| trafilatura | 0.696 | 0.335 | 0.917 | 0.788 | 0.564 | 0.653 | 0.768 |
| Pulpie (L4 GPU) | 0.803 | 0.553 | 0.953 | 0.869 | 0.756 | 0.660 | 0.894 |

## By page type: include

| system | article | collection | documentation | forum | listing | product | service |
|---|---|---|---|---|---|---|---|
| Gradient booster | 0.883 | 0.900 | 0.961 | 0.903 | 0.922 | 0.922 | 0.950 |
| Logistic regression | 0.861 | 0.456 | 0.956 | 0.783 | 0.878 | 0.767 | 0.889 |
| Sequence model (BiGRU) | 0.717 | 0.344 | 0.917 | 0.722 | 0.728 | 0.667 | 0.883 |
| trafilatura | 0.661 | 0.344 | 0.900 | 0.717 | 0.506 | 0.633 | 0.711 |
| Pulpie (L4 GPU) | 0.906 | 0.756 | 0.978 | 0.861 | 0.836 | 0.578 | 0.894 |

## By page type: exclude

| system | article | collection | documentation | forum | listing | product | service |
|---|---|---|---|---|---|---|---|
| Gradient booster | 0.922 | 0.928 | 0.933 | 0.889 | 0.844 | 0.889 | 0.952 |
| Logistic regression | 0.806 | 0.867 | 0.922 | 0.967 | 0.889 | 0.911 | 0.940 |
| Sequence model (BiGRU) | 0.967 | 0.956 | 0.978 | 0.967 | 0.939 | 0.956 | 0.964 |
| trafilatura | 0.894 | 0.856 | 0.900 | 0.950 | 0.911 | 0.922 | 0.952 |
| Pulpie (L4 GPU) | 0.894 | 0.933 | 0.983 | 0.978 | 0.878 | 0.961 | 0.964 |

## By page type: structure

| system | article | collection | documentation | forum | listing | product | service |
|---|---|---|---|---|---|---|---|
| Gradient booster | 0.640 | 0.795 | 0.873 | 0.640 | 0.860 | 0.837 | 0.903 |
| Logistic regression | 0.717 | 0.508 | 0.870 | 0.478 | 0.702 | 0.748 | 0.773 |
| Sequence model (BiGRU) | 0.418 | 0.243 | 0.735 | 0.413 | 0.539 | 0.464 | 0.749 |
| trafilatura | 0.213 | 0.116 | 0.652 | 0.288 | 0.206 | 0.335 | 0.339 |
| Pulpie (L4 GPU) | 0.767 | 0.874 | 0.689 | 0.747 | 0.802 | 0.662 | 0.749 |

## By page type: QA evidence proxy

| system | article | collection | documentation | forum | listing | product | service |
|---|---|---|---|---|---|---|---|
| Gradient booster | 0.875 | 0.722 | 0.969 | 0.842 | 0.825 | 0.775 | 0.886 |
| Logistic regression | 0.819 | 0.375 | 0.981 | 0.739 | 0.750 | 0.589 | 0.797 |
| Sequence model (BiGRU) | 0.658 | 0.228 | 0.944 | 0.767 | 0.678 | 0.469 | 0.819 |
| trafilatura | 0.697 | 0.222 | 0.911 | 0.642 | 0.333 | 0.467 | 0.636 |
| Pulpie (L4 GPU) | 0.842 | 0.617 | 0.956 | 0.792 | 0.681 | 0.408 | 0.844 |

## By page type: block-level char F1

| system | article | collection | documentation | forum | listing | product | service |
|---|---|---|---|---|---|---|---|
| Gradient booster | 0.873 | 0.889 | 0.933 | 0.947 | 0.936 | 0.848 | 0.952 |
| Logistic regression | 0.867 | 0.539 | 0.980 | 0.928 | 0.920 | 0.859 | 0.903 |
| Sequence model (BiGRU) | 0.852 | 0.450 | 0.972 | 0.923 | 0.894 | 0.779 | 0.926 |
| trafilatura | 0.919 | 0.416 | 0.936 | 0.911 | 0.356 | 0.762 | 0.795 |

## Runtime

CPU systems: Apple-silicon laptop CPU, one process, pages sequential, single-threaded inference, after a warm-up page; time covers raw HTML to markdown (classifiers include segmentation, their own trafilatura run for the agreement features, features, inference and rendering). Pulpie: per-page GPU time on one Modal L4 (batch size 1, cuda-synchronized, after warm-up).

| system | hardware | mean ms | median ms | p95 ms | pages / s |
|---|---|---|---|---|---|
| Gradient booster | CPU (1 core) | 106 | 73 | 274 | 9.4 |
| Logistic regression | CPU (1 core) | 96 | 65 | 257 | 10.4 |
| Sequence model (BiGRU) | CPU (1 core) | 100 | 69 | 260 | 10.0 |
| trafilatura | CPU (1 core) | 62 | 35 | 205 | 16.2 |
| Pulpie (L4 GPU) | GPU L4 | 374 | 264 | 1091 | 2.7 |

Pulpie run: model load 1.8 s, container startup 4.6 s, 2 container(s), billed GPU time ≈ 145 s (≈ $0.033).

Projected compute cost per 1 million pages at the measured throughput (Modal list prices: L4 $0.000222/s, CPU $1.31e-05/core/s; memory and orchestration excluded, no batching or parallelism assumed):

| system | compute per 1M pages | cost per 1M pages |
|---|---|---|
| Gradient booster | 29 core-hours | $1.39 |
| Logistic regression | 27 core-hours | $1.26 |
| Sequence model (BiGRU) | 28 core-hours | $1.31 |
| trafilatura | 17 core-hours | $0.81 |
| Pulpie (L4 GPU) | 104 GPU-hours | $83.03 |

## Notes

- One must_include snippet cannot be matched even in the golden markdown under this normalization (1,212 / 1,213), so the ceiling for include is just under 1.
- Empty outputs: Gradient booster 0, Logistic regression 0, Sequence model (BiGRU) 7, trafilatura 0, Pulpie (L4 GPU) 0 (scored as empty).
- The BiGRU's frozen threshold (0.69) is the highest of the three, which is why it returns empty output on some pages.
- References are model-generated; scores measure agreement with that reference, not human judgment.
- **Reference bias in favor of the three classifiers:** the test references come from the same Gemini block-labeling pipeline (same rubric, same segmentation as `models/blocking.py`) that produced the 140 labeled training pages, and 207 of 210 test pages share a domain with training pages. trafilatura and Pulpie were never trained on this labeler, so their gap is partly a label-convention gap. The classifier vs classifier comparison is fair; the classifier vs trafilatura/Pulpie margin is an upper bound.
