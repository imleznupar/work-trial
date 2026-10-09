# Block lens

From the repository root:

```sh
.venv/bin/python demo/server.py
```

Open http://127.0.0.1:8000. Use `--port 8001` to choose another port.

Paste HTML or upload a file, then click **Analyze blocks**. The demo compares the actual frozen logistic regression, gradient boosting, and BiGRU sequence models with the Trafilatura heuristic baseline. It shows every segmented block, keep/drop decisions, probabilities, disagreements, and extracted text. Results can be downloaded as JSON.

The three models use their frozen thresholds. Trafilatura is mapped onto the same blocks with `features.page_features(...).in_traf`, the repository's existing fuzzy text/table matching rule. These mapped decisions are an approximation of its extraction; choose **Trafilatura · original extraction** to see the baseline's original output.

The demo reuses the repository's Python environment and frozen model artifacts, runs on localhost, and never renders submitted HTML as executable markup. No hosting or frontend build is required.
