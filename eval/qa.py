"""Model-based QA on the saved outputs (eval/outputs/{system}/{page_id}.md) for the 673 test QAs.

Answer: gemini-3.8-flash, temperature 0, low thinking; sees only that system's markdown and the question; must answer
concisely from the text or reply exactly NOT FOUND. Outputs over MAX_CHARS are truncated from the end (recorded).
Grade: NOT FOUND -> NOT_FOUND without a call; otherwise a separate grader call (same model, temperature 0) that sees
only the question, the expected answer, the required answer points and the candidate answer -> CORRECT / INCORRECT /
NOT_FOUND. The grader never sees the system name.
Robustness: 60 s HTTP timeout, 6 concurrent calls, up to 6 retries with backoff, every error logged to
eval/results/qa_errors.log; an item that still fails is recorded as API_ERROR (counted as not correct).
Cache: eval/qa_cache/{answers,grades}/..., keyed by system, page, question index and the output's sha256.
Writes eval/results/qa_results.csv and eval/results/qa_usage.json.
"""
import csv
import hashlib
import json
import os
import random
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import common as E

MODEL = "gemini-3.8-flash"
CACHE = E.EVAL / "qa_cache"
MAX_CHARS = 3_500_000
PRICE_IN, PRICE_OUT = 0.75, 3.75  # USD per 1M tokens, ai.google.dev/gemini-api/docs/pricing (through 2026-12-31)
ANSWER = ("You are given the text of a web page converted to markdown, and a question. Answer the question concisely "
          "using only the provided text. Do not use outside knowledge. If the text does not contain the answer, reply "
          "exactly: NOT FOUND")
GRADE = ("You grade a candidate answer to a question about a web page. You are given the question, the expected answer, "
         "the required answer points, and the candidate answer. Reply with exactly one word:\n"
         "CORRECT - the candidate states every required answer point (wording may differ; extra detail is fine) and "
         "does not contradict the expected answer\n"
         "INCORRECT - the candidate misses a required point, is wrong, or contradicts the expected answer\n"
         "NOT_FOUND - the candidate declines or says the information is not available")
_lock, _client = threading.Lock(), None
ERRLOG = E.RESULTS / "qa_errors.log"


def client():
    global _client
    if _client is None:
        from google import genai
        from google.genai import types
        _client = genai.Client(api_key=os.environ["GEMINI_API_KEY"], http_options=types.HttpOptions(timeout=60000))
    return _client


def call(instr, contents, tag):
    from google.genai import types
    cfg = types.GenerateContentConfig(temperature=0, system_instruction=instr,
                                      thinking_config=types.ThinkingConfig(thinking_level="low"))
    for attempt in range(7):
        try:
            r = client().models.generate_content(model=MODEL, contents=contents, config=cfg)
            u = r.usage_metadata
            return {"text": (r.text or "").strip(), "in": u.prompt_token_count or 0, "out": u.candidates_token_count or 0,
                    "thoughts": u.thoughts_token_count or 0, "model_version": r.model_version}
        except Exception as e:  # noqa: BLE001
            with _lock, open(ERRLOG, "a") as f:
                f.write(f"{time.strftime('%H:%M:%S')} {tag} attempt {attempt}: {type(e).__name__}: {str(e)[:300]}\n")
            if attempt == 6:
                return None
            time.sleep(min(60, 2 ** attempt + random.random()))


def cached(path, fn):
    if path.exists():
        return json.loads(path.read_text())
    r = fn()
    if r is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(r, ensure_ascii=False))
    return r


def not_found(a):
    return re.sub(r"[^a-z]", "", a.lower()) == "notfound"


def job(item):
    system, pid, qi, q = item
    md = (E.OUT / system / f"{pid}.md").read_text(encoding="utf-8")
    h = hashlib.sha256(md.encode()).hexdigest()[:12]
    text = md[:MAX_CHARS]
    tag = f"{system}/{pid}/{qi}"
    ans = cached(CACHE / "answers" / system / f"{pid}__{qi}__{h}.json",
                 lambda: call(ANSWER, f"Text:\n<<<\n{text}\n>>>\n\nQuestion: {q['question']}", tag + " answer"))
    row = {"system": system, "page_id": pid, "q_index": qi, "difficulty": q.get("difficulty"),
           "question": q["question"], "expected": q["expected_answer"], "truncated": len(md) > MAX_CHARS}
    if ans is None:
        return {**row, "answer": "", "verdict": "API_ERROR", "grader": ""}
    cand = ans["text"]
    if not_found(cand):
        return {**row, "answer": cand, "verdict": "NOT_FOUND", "grader": "rule"}
    points = "\n".join(f"- {p}" for p in q.get("required_answer_points") or [])
    gk = hashlib.sha256(f"{q['question']}|{q['expected_answer']}|{points}|{cand}".encode()).hexdigest()[:20]
    g = cached(CACHE / "grades" / f"{gk}.json",
               lambda: call(GRADE, f"Question: {q['question']}\nExpected answer: {q['expected_answer']}\n"
                                   f"Required answer points:\n{points}\nCandidate answer: {cand}", tag + " grade"))
    if g is None:
        return {**row, "answer": cand, "verdict": "API_ERROR", "grader": ""}
    v = re.sub(r"[^A-Z_]", "", g["text"].upper())
    verdict = next((x for x in ("NOT_FOUND", "INCORRECT", "CORRECT") if v.startswith(x)), "UNPARSED")
    return {**row, "answer": cand, "verdict": verdict, "grader": g["text"][:40]}


def main():
    E.RESULTS.mkdir(parents=True, exist_ok=True)
    systems = sys.argv[1].split(",") if len(sys.argv) > 1 else E.SYSTEMS
    items = [(s, a["page_id"], i, q) for a in E.annotations() for i, q in enumerate(a["qa_questions"]) for s in systems]
    print(f"{len(items)} (system, question) items", flush=True)
    t0, rows = time.time(), []
    with ThreadPoolExecutor(6) as ex:
        for i, r in enumerate(ex.map(job, items), 1):
            rows.append(r)
            if i % 250 == 0:
                print(f"{i}/{len(items)} {time.time() - t0:.0f}s", flush=True)
    with open(E.RESULTS / "qa_results.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    usage = {}
    for k in ("answers", "grades"):
        fs = [json.loads(p.read_text()) for p in (CACHE / k).rglob("*.json")]
        u = {"calls": len(fs), "in": sum(x["in"] for x in fs), "out": sum(x["out"] for x in fs),
             "thoughts": sum(x["thoughts"] for x in fs)}
        u["usd"] = (u["in"] * PRICE_IN + (u["out"] + u["thoughts"]) * PRICE_OUT) / 1e6
        usage[k] = u
    usage["total_usd"] = usage["answers"]["usd"] + usage["grades"]["usd"]
    usage["model"], usage["pricing_usd_per_1M"] = MODEL, {"input": PRICE_IN, "output_incl_thinking": PRICE_OUT}
    (E.RESULTS / "qa_usage.json").write_text(json.dumps(usage, indent=1))
    from collections import Counter
    print(Counter(r["verdict"] for r in rows), f"| {time.time() - t0:.0f}s | usage {json.dumps(usage)}")


if __name__ == "__main__":
    main()
