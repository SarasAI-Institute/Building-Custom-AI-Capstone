# RiskLens Capstone: Grading Rubric

## Total Score: 100 Points

| Week | Focus | Weight |
|------|-------|--------|
| 1 | VLM Defect Inspector | 25% |
| 2 | RAG Evidence Engine | 25% |
| 3 | Fine-Tuned Analyst | 25% |
| 4 | Compression, Gate & Assembly | 25% |

### Grading Scheme

| Grade | Requirement |
|-------|-------------|
| **Satisfactory (S)** | Total score ≥ 70% |
| **Unsatisfactory (U)** | Total score < 70% |

Grading is a **manual review of the submitted notebook link with saved outputs** — graders do
not re-run training. Each stage ends in a `📊 EVALUATION` cell that computes the stage's
metrics; an evaluation cell with no saved output = deliverable not demonstrated.

---

## Week 1: VLM Defect Inspector (25 Points)

### Deliverables
- [ ] D1.1 Frozen split: ≥40 test images (≥20/class) + dev set, built before any prompt work
- [ ] D1.2 All 3 baseline bugs diagnosed (symptom → root cause → fix, one markdown cell each)
- [ ] D1.3 `inspect()` honoring the JSON contract, never raises
- [ ] D1.4 Prompt ladder: ≥3 iterations incl. one few-shot attempt, dev accuracy each
- [ ] D1.5 Error analysis: ≥3 misclassified test images with hypotheses
- [ ] D1.6 Evaluation cell run, outputs saved — beats `inspect_v0` on defect **F1** (the baseline's recall is inflated by BUG-1 — diagnosing that is D1.2); cost/1k recorded
- [ ] D1.7 Resolution-budget experiment: dev accuracy + sec/image at ≥3 image sizes, with a production recommendation

### Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Bug Fixes** | 9 | All 3 baseline bugs found, explained, and fixed (3 pts each: negation-unsafe parser, context-free prompt, starved JSON contract) |
| **Inspector Quality** | 8 | `inspect()` beats baseline defect F1 (4); prompt ladder with dev numbers, few-shot attempted (4) |
| **Evaluation Discipline** | 5 | Split frozen before iteration (cell order), ≥40 test images, evaluation cell run with confusion matrix + cost/1k; resolution-budget table (D1.7) with a recommendation |
| **Error Analysis & Clarity** | 3 | Misclassifications shown with plausible hypotheses; workspace readable |

---

## Week 2: RAG Evidence Engine (25 Points)

### Deliverables
- [ ] D2.1 Corpus: ≥100 real reviews (provenance stated) + the 4 official `CAPSTONE_DOCS` verbatim + ≥2 authored docs with planted facts
- [ ] D2.2 Frozen gold set: ≥20 questions, ≥3 multi-hop, authored before indexing
- [ ] D2.3 `retrieve()` beats `retrieve_v0` on recall@4
- [ ] D2.4 `rag_answer()` with citations + refusal rule (must use a given `REFUSAL_PHRASES` phrase); ≥4/5 adversarial questions refused
- [ ] D2.5 Faithfulness + answer-relevance scored, judge caveats stated
- [ ] D2.6 Evaluation cell run, outputs saved — baseline-vs-yours recall table + refusal rate
- [ ] D2.7 One measured retrieval upgrade beyond the prefix (chunking / reranker / hybrid / k-sweep): before/after recall table + adopt/reject verdict

### Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Retrieval Quality** | 8 | Beats baseline on recall@4 (4); the D2.7 upgrade experiment measured before/after with an adopt/reject verdict (4) |
| **Grounded Generation** | 7 | Citations correct (3); refusal rule survives the adversarial set ≥4/5 (4) |
| **Evaluation Discipline** | 7 | Gold set ≥20 with ≥3 multi-hop, authored before the index (4); faithfulness + relevance scored with caveats (3) |
| **Corpus Craft & Clarity** | 3 | Authored docs contain planted, testable facts incl. one cross-document link; workspace readable |

---

## Week 3: Fine-Tuned Analyst (25 Points)

### Deliverables
- [ ] D3.1 ≥150 pairs from a real teacher model (template generator not accepted)
- [ ] D3.2 Dataset card complete; dedup + decontamination shown as actions
- [ ] D3.3 Frozen `analyst_test_rows` ≥25; leakage certificate ≤0.90
- [ ] D3.4 QLoRA trained; adapter saved / Hub-linked
- [ ] D3.5 Three-way eval: format · rubric score (stronger judge) · blind randomized win-rate
- [ ] D3.6 Evaluation cell run, outputs saved; `WEEK3_RESULTS` filled
- [ ] D3.7 Ablation: ONE training knob changed (r / epochs / LR / data size), retrained, compared on the frozen set, one-paragraph conclusion

### Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Dataset Engineering** | 9 | Real teacher + varied generation (4); dedup and decontamination performed with counts (3); complete dataset card (2) |
| **Fine-Tune** | 6 | QLoRA config sane for hardware, training completed, loss curve commented, adapter saved (3); D3.7 ablation with both runs' frozen-set numbers + conclusion (3) |
| **Evaluation Discipline** | 7 | Frozen ≥25 rows + leakage certificate (3); all three metrics present — format, rubric with judge caveats, win-rate with randomized A/B (4) |
| **Honest Reporting** | 3 | Same-distribution and judge-bias caveats stated; OOD failure prediction concrete |

---

## Week 4: Compression, Gate & Assembly (25 Points)

### Deliverables
- [ ] D4.1 GATE committed before any re-score (cell order is evidence)
- [ ] D4.2 ≥2 compression arms with memory footprints
- [ ] D4.3 Re-score: format + content vs Stage 3; verdict stated even if FAIL
- [ ] D4.4 p50/p95 + true-token tok/s + $/1k; hardware-dependence sentence
- [ ] D4.5 `analyze_product()` demoed on ≥3 products (≥1 good, ≥2 defective) with saved outputs
- [ ] D4.6 Deployment note: target runtime, what breaks at 100×, monitoring signal
- [ ] D4.7 Batch stress test: full pipeline over ≥10 products — end-to-end p50/p95, stage-time breakdown, failure taxonomy

### Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Pipeline Assembly** | 8 | All three stages compose through the contracts; ≥3 product demos saved (4); D4.7 stress test with stage-time breakdown + failure taxonomy (4) |
| **Quality Gate** | 7 | Threshold committed before measurement (3); format AND content re-scored on the frozen set, verdict honest (4) |
| **Compression & Economics** | 7 | ≥2 arms with memory numbers (3); honest latency/throughput + $/1k (4) |
| **Deployment Thinking** | 3 | Runtime choice justified; failure-at-scale + monitoring signal named |

---

## Grading Scale

| Grade | Score | Description |
|-------|-------|-------------|
| **Satisfactory (S)** | ≥ 70 | Meets requirements, demonstrates competency |
| **Unsatisfactory (U)** | < 70 | Does not meet minimum requirements |

> **Note:** You need at least 70 points (70%) to pass the project.

---

## Automatic Deductions

| Issue | Deduction |
|-------|-----------|
| Notebook doesn't run top-to-bottom at final delivery | −10 points |
| Missing Week-5 delivery (run-all + holdout submission + reflection) | −10 points |
| Missing week deliverable (stage not attempted) | −25 points (full week) |
| Eval smell: frozen artifact authored *after* build cells (split/gold/card/gate) | −5 points per instance |
| Eval smell: win-rate without randomized A/B, or judge = generator with no caveat | −3 points per instance |
| Late submission (per day) | −5 points |
| Plagiarism / copied notebook | −100 points |

---

## Bonus Points (Up to 10 extra)

| Bonus | Points | Description |
|-------|--------|-------------|
| Hidden-holdout composite ≥ 0.60 | +3 | Robustness on data you never saw (≤3 submissions) |
| GGUF export actually served (llama.cpp / Ollama, screenshot or log) | +2 | The full CPU/edge lane, working |
| Deployed demo (HF Space or equivalent, link works) | +2 | The pipeline has a URL |
| Second MVTec category or own images in Stage 1 | +1 | Generalization beyond the default |
| DPO pass or distillation experiment on the Analyst, with before/after numbers | +2 | A Week-4 technique applied for real |

---

## Submission Requirements

Each week, submit:
1. The notebook link (same link every week — Colab/Kaggle/nbviewer with saved outputs)
2. Brief summary of what you completed
3. Any notes or known issues

**The notebook must include:**
- All 📊 evaluation cells run, outputs saved
- The metrics ledger (`capstone_metrics.json` contents visible via `show_ledger()`)
- Frozen artifacts above workspaces (cell order intact)

---

## Questions?

Reach out to your instructor or post in the course forum.

Good luck! 🚀
