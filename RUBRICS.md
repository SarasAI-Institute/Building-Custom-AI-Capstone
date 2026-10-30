# RiskLens competency rubric

**Criterion Set v2.0 · five competencies · 24 required criteria.** This is a readable transcription of the supplied consolidated rubric. The source PDFs are preserved in [assessment/reference](assessment/reference/). The consolidated standard governs assessment criteria; published course policy governs administration.

Each criterion is **Met** or **Not Yet**. A competency is **Mastered** only when every criterion in that competency is Met. The project is Mastered only when all five competencies are Mastered. Technical metrics are evidence, not course grades. There are no points, averages, deductions or bonus credits.

Review the module's **MUST PASS** criterion first. If it is Not Yet, return targeted feedback before reviewing the other criteria. Those criteria are still required; the gate changes review order, not weight.

| Module | Competency | Criteria | Notebook evidence | Review first |
|---|---|---|---|---|
| 1 | Visual Inspection and Evaluation | C1.1–C1.5 | D1.1–D1.7 | C1.1 |
| 2 | Grounded Retrieval and Generation | C2.1–C2.5 | D2.1–D2.7 | C2.3 |
| 3 | Model Adaptation and Evaluation | C3.1–C3.5 | D3.1–D3.7 | C3.2 |
| 4 | Model Optimization and Deployment Decisions | C4.1–C4.5 | D4.1–D4.4 | C4.2 |
| 5 | Integrated System Delivery and Defense | C5.1–C5.4 | D4.5–D4.7 + final delivery | C5.1 |

## Evidence and revision

Submit the same continuing notebook link at each module milestone, with saved outputs, a short completion summary and known issues. Keep a dated snapshot. Graders assess saved evidence and accessible artifacts; they need not repeat training. A cell's position is not proof of when it ran. Preserve real prompts, configurations, data versions and outputs as the work happens.

Return inaccessible or incomplete submissions for correction before assessment. Missing evaluation output, broken run/load paths and exposed credentials need correction. Refer fabricated measurements, reconstructed evidence or copied work under academic-integrity policy; do not invent numerical penalties.

Feedback names each Not Yet criterion, the missing/incorrect evidence and the required revision. Reassess those criteria and previously Met evidence affected by the changes. Attempt limits, waiting periods, enrollment rules and formal grade codes follow published course policy.

GraphRAG/KAG implementations, independent distillation, multi-parent merging, multi-GPU training, GGUF serving, hosted demos and additional categories are optional. They cannot compensate for missing required evidence. This rubric adds no hidden-holdout score, timed exam or recorded-defense rule.

## C1 — Module 1

### C1.1 Your evaluation split is frozen — MUST PASS

**Evidence:** D1.1 SPLIT cell; saved seed/counts; pre-iteration notebook snapshot or version history.

**Met:** Before prompt iteration, freeze at least 40 test images with at least 20 per class and a separate development set. Print seed, membership identifiers and class counts. Preserve a dated snapshot or version record. Use development data for choices and disclose any later test exposure.

**Common mistakes:** Changing the split after seeing results; overlapping development and test images; treating cell position alone as proof of timing.

### C1.2 Your inspector fixes the inherited defects

**Evidence:** D1.2 bug diagnoses; D1.3 inspect(); representative outputs and fallback checks.

**Met:** Diagnose and fix the negation-unsafe parser, context-free prompt and empty defect description. Each diagnosis links a real symptom to its cause and fix. inspect() returns the required JSON fields and valid verdict, uses a domain prompt and structured output, and handles malformed model replies without an uncaught parsing error. Justify the VLM choice.

**Common mistakes:** Leaving one bug unresolved; treating "no defects" as defective; returning empty defect evidence; a parser failure that crashes the pipeline.

### C1.3 Your prompt iteration is measured

**Evidence:** D1.3-D1.4 prompt ladder; saved development outputs.

**Met:** Compare at least three prompt iterations on the same development set, including a few-shot attempt. Keep every prompt, development accuracy, reason for the change and final selection visible. Include the few-shot token-cost observation. Select the final prompt before final-test scoring.

**Common mistakes:** Only showing the winning prompt; unmeasured prompt changes; choosing a prompt from test-set results; omitting the few-shot attempt.

### C1.4 Your performance and error claims are supported

**Evidence:** D1.5 images and analysis; D1.6 saved Stage 1 evaluation and ledger.

**Met:** On the frozen test set, report baseline and final defect F1 and the confusion matrix; final F1 exceeds inspect_v0. Analyze at least three actual errors with plausible hypotheses. If fewer exist, analyze all errors and enough clearly labeled borderline cases to total three. Save the evaluation outputs and explain the baseline recall inflation.

**Common mistakes:** Comparing different test sets; substituting accuracy or recall for defect F1; inventing errors; reporting numbers without saved outputs.

### C1.5 Your resource recommendation follows the evidence

**Evidence:** D1.6 timing/cost; D1.7 resolution table and recommendation.

**Met:** Measure development accuracy and seconds per image at three or more image sizes under stated hardware and settings. Record estimated cost per 1,000 inspections with the assumed hourly price. Recommend an image size based on the observed quality/time trade-off and explain what the processor actually does with the resized inputs.

**Common mistakes:** Only reporting memory; comparing different image sets; claiming higher input resolution always helps; omitting price or runtime assumptions.

All criteria above must be Met.

## C2 — Module 2

### C2.1 Your corpus and gold questions are valid

**Evidence:** D2.1 CORPUS; D2.2 GOLD; source provenance and frozen snapshot.

**Met:** Include at least 100 real reviews, all four official documents verbatim with their IDs, and at least two authored documents containing testable facts and a cross-document link. Before indexing, freeze at least 20 corpus-based gold questions, including three multi-hop cases, with required source IDs and reference answers. Preserve the version record.

**Common mistakes:** Invented reviews presented as real; altered official facts; gold questions chosen after retrieval trials; multi-hop labels on single-source questions.

### C2.2 Your retriever improves under a fair comparison

**Evidence:** D2.3 retrieve(); D2.6 evaluation; D2.7 upgrade experiment.

**Met:** Beat retrieve_v0 on recall@4 using the same corpus, frozen gold questions and metric implementation. Save baseline/final recall at k = 1, 2, 4 and 8. Measure one upgrade beyond the query prefix on unchanged questions, show before/after results, and justify adopting or rejecting it. A rejected upgrade is valid evidence.

**Common mistakes:** Changing the gold set or corpus between arms; claiming recall@8 beats baseline recall@4; reporting only the prefix fix; omitting a negative experiment.

### C2.3 Your answers are grounded and refuse unsupported claims — MUST PASS

**Evidence:** D2.4 rag_answer(); answer/hit pairs; five-question adversarial set and saved responses.

**Met:** Return the answer and the actual retrieved hits. Citations resolve to those source IDs and support the associated claims. Preselect five genuinely unanswerable questions; at least four receive a refusal containing a REFUSAL_PHRASES phrase without an invented answer. Report all five outcomes; separately report any additional adversarial cases.

**Common mistakes:** Decorative or nonexistent citations; refusing and then inventing an answer; changing adversarial questions after seeing failures; counting a phrase match as sufficient proof.

### C2.4 Your generation evaluation measures both axes

**Evidence:** D2.5 scoring outputs; D2.6 evaluation and ledger; judge protocol.

**Met:** Score faithfulness and answer relevance separately over the frozen gold set. State the judge or evaluation tool, scoring instructions, sample size and aggregation, and preserve representative answer-level results. Explain judge bias, especially shared generator/judge weights. Save the Stage 2 outputs and ledger; reference-substring matches alone do not establish faithfulness.

**Common mistakes:** Only measuring retrieval; using answer-substring matches as a faithfulness score; unnamed judge; no caveat about self-evaluation or judgment limits.

### C2.5 Your retrieval design choice is justified

**Evidence:** Design note beside D2.7; one question and its linked source IDs.

**Met:** Trace a question requiring linked facts across documents. Explain whether graph-assisted retrieval would help and identify its extraction, indexing and maintenance costs. Distinguish the notebook graph-hop illustration from full GraphRAG and KAG systems. Justify the retrieval approach used in RiskLens; implementing a complete graph framework is not required.

**Common mistakes:** Calling any vector index GraphRAG; presenting a toy graph as a complete KAG system; claiming graphs improve every query; no concrete linked question.

All criteria above must be Met.

## C3 — Module 3

### C3.1 Your training data is real and curated

**Evidence:** D3.1 teacher calls and examples; D3.2 DATASET_CARD and cleaning counts.

**Met:** Generate at least 150 raw pairs with a named real teacher model and varied inputs using make_input(). Document the generation strategy. Perform deduplication and train/test decontamination, printing before/after and removal counts. Complete every dataset-card field and report retained training size. Template-only generated reports do not meet the requirement.

**Common mistakes:** Using the practice template as teacher output; claiming 150 retained examples when only raw count was measured; describing cleaning without running it; incomplete card.

### C3.2 Your evaluation data is separated from training — MUST PASS

**Evidence:** D3.3 analyst_test_rows; similarity calculation; dataset-card snapshot before training.

**Met:** Freeze at least 25 Analyst test rows before training. Drop contaminated training rows and show the maximum train-to-test cosine similarity is at most 0.90 using a declared embedding model and method. Preserve the frozen version and counts. Explain that the similarity screen is a leakage heuristic, not proof of independence.

**Common mistakes:** Training on evaluation examples; removing inconvenient test rows; reporting the mean instead of maximum similarity; using cell order as the only chronology evidence.

### C3.3 Your QLoRA adapter is trained and reloadable

**Evidence:** D3.4 training configuration, loss outputs, adapter artifact and reload demonstration.

**Met:** Complete QLoRA training with a configuration appropriate to the runtime. Preserve base model ID/revision, adapter settings and training parameters, and interpret the observed loss. Save the learner-trained adapter to an accessible path or Hub location and demonstrate loading it. The delivery path loads saved weights instead of retraining on every Run all.

**Common mistakes:** A configuration with no completed training; an adapter path that is inaccessible; loading only the base; no loss interpretation; retraining unexpectedly during delivery.

### C3.4 Your base and tuned comparison is valid

**Evidence:** D3.5 generations and judgments; D3.6 WEEK3_RESULTS, Stage 3 output and ledger.

**Met:** Evaluate genuinely untuned base and tuned outputs on the same frozen rows using format adherence, content rubric scores and blind randomized A/B judgments. Name a separate, stronger judge and state its limitations. Show wins, losses, ties and denominator. Populate WEEK3_RESULTS from saved evidence. No minimum win-rate or tuning-improvement margin is imposed.

**Common mistakes:** The base still has an active adapter; fixed A/B position; a percentage without counts; judge equals generator without disclosure; scores copied without supporting outputs.

### C3.5 Your ablation supports a defensible conclusion

**Evidence:** D3.7 two adapter runs, configuration difference, comparison and conclusion.

**Met:** Change exactly one training variable: rank, epochs, learning rate or training-data size. Train a second adapter and compare both runs on the same frozen rows with the same evaluation protocol. Preserve both results. Explain what changed, whether tuning is justified, a specific expected out-of-distribution failure and the limits of using the frozen set for repeated comparisons.

**Common mistakes:** Multiple variables changed; no retraining; comparing different evaluation rows; hiding worse results; generic claims about generalization without a concrete failure case.

All criteria above must be Met.

## C4 — Module 4

### C4.1 Your optimization choice shows understanding

**Evidence:** Technique note beside D4.1-D4.2; links to the selected model configurations.

**Met:** Distinguish data from model parallelism, training from inference optimization, teacher-output from logit distillation, adapter folding from multi-model merging, and reduced-precision quantization. Identify the RiskLens bottleneck and justify the chosen route and trade-offs. Independent multi-GPU training, distillation and multi-parent merging are optional extensions, not required implementations.

**Common mistakes:** Calling device placement data-parallel training; confusing adapter folding with merging several fine-tunes; claiming compression always accelerates inference; listing terms without a choice.

### C4.2 Your quality gate precedes the comparison — MUST PASS

**Evidence:** D4.1 GATE and pre-score snapshot/version; baseline and candidate inventory.

**Met:** Before compressed-model re-scoring, record justified maximum format and content drops, their units, the Stage 3 reference, candidate arms, hourly price and intended ship arm. Preserve the dated version; keep thresholds unchanged for that comparison. Explain why the tolerances are acceptable for the stated use case rather than choosing them to guarantee a pass.

**Common mistakes:** Setting thresholds after seeing results; confusing percent with percentage points; changing the intended arm without a separate decision record; unjustified permissive tolerances.

### C4.3 Your compression comparison uses the trained Analyst

**Evidence:** D4.2 memory table; D4.3 saved generations, quality table and Module 4 checkpoint.

**Met:** Produce at least two compression arms of the learner-trained Analyst and record memory footprints and ratios against half precision. Re-score each arm and the Stage 3 reference on the same frozen rows for format and content, with consistent settings. Show threshold comparisons and every verdict. Identify content cosine similarity as a proxy, not factual correctness.

**Common mistakes:** Quantizing an untuned base; counting a configuration as a measured arm; measuring format only; different rows per arm; presenting cosine similarity as a factuality guarantee.

### C4.4 Your serving estimates are measured and qualified

**Evidence:** D4.4 benchmark outputs for reference and each arm; settings and cost calculation.

**Met:** Report p50/p95 latency, actual generated-token throughput and estimated cost per 1,000 reports for the reference and each arm. State hardware, run count, warm-up, input/output lengths and hourly-price/utilization assumptions. Label small-sample percentiles and cost estimates appropriately; explain why lower precision may save memory without reducing latency.

**Common mistakes:** Using max_new_tokens as generated length; comparing unequal workloads without disclosure; calling notebook p95 a production SLA; treating the assumed GPU price as a verified bill.

### C4.5 Your deployment decision respects the gate

**Evidence:** D4.3 decision note; accepted/rejected arm inventory; fallback and limits.

**Met:** Select a candidate that passes the declared gate or reject failed candidates and document a feasible fallback. Link the decision to quality, memory and runtime evidence. An honestly evaluated failed compression can meet this competency; it cannot be labeled production-ready. Keep the original gate record and distinguish any later candidate or fallback evaluation.

**Common mistakes:** Declaring ship after a failed gate; hiding a quality drop behind a smaller file; silently changing the model; rewriting the threshold to make a candidate pass.

All criteria above must be Met.

## C5 — Module 5

### C5.1 Your real components work together — MUST PASS

**Evidence:** D4.5 analyze_product(); three saved product demonstrations; selected Analyst record.

**Met:** Compose the learner inspector, retriever and selected Analyst through the published contracts. Preserve the GOOD short-circuit and return note, evidence and report. Save at least three product demonstrations: one good and two defective, with traceable inputs and outputs. Use real components, not hard-coded substitutes. Label any fallback or failed-gate demonstration and its limits.

**Common mistakes:** Demo stubs standing in for components; a JSON note passed where training used prose; missing good-product behavior; reports with no traceable evidence; a rejected model labeled ready.

### C5.2 Your system evaluation locates failures

**Evidence:** D4.7 batch outputs; timing table; product-level failure taxonomy.

**Met:** Run the full pipeline on at least ten products and save end-to-end p50/p95 plus inspector, retrieval and Analyst timing. For every wrong or weak report, identify the responsible stage and evidence for that diagnosis; explicitly report if none are observed. Explain what the small workload cannot establish about production reliability or generalization.

**Common mistakes:** Benchmarking only the Analyst; no stage timing; vague failure categories; silently skipping failures; claiming a small batch establishes production reliability.

### C5.3 Your delivery is reproducible and documented

**Evidence:** D4.6 deployment note; final run/load and show_ledger(); artifacts, environment and reflection.

**Met:** Provide a clean top-to-bottom run/load with saved evaluation outputs, accessible model/data artifacts and environment/configuration details. Display the complete metrics ledger and preserve earlier comparisons separately. Document runtime choice, the bottleneck at 100 times traffic and a monitoring signal. Include a reflection of at most 300 words on trade-offs, trusted/uncertain numbers and next steps.

**Common mistakes:** Missing weights or data; a notebook that depends on hidden state; outputs cleared; assuming overwritten ledger entries preserve all experiments; deployment claims without a runnable route.

### C5.4 You can explain the submitted system

**Evidence:** Explanation cells in final notebook; traceable code/outputs; exam evidence if separately issued.

**Met:** Explain what one actual component does, why its design fits RiskLens and what would break if a named part were removed. Trace one demonstrated product through the applicable stages. Defend one reported metric and discuss a failed experiment or unsupported claim using saved evidence. Submit a written walkthrough; separately issued exam evidence may replace equivalent parts.

**Common mistakes:** Reading code without explaining behavior; a generic architecture unrelated to the notebook; no supporting measurement; avoiding a failure or limitation; substituting polish for understanding.

All criteria above must be Met.

## Metric and sequencing clarifications

- **C1:** Analyze three real errors; if fewer occur, analyze all errors and enough explicitly labeled borderline cases to total three. Never manufacture errors.
- **C2:** The named recall@k metric is the fraction of questions for which **all required source IDs** appear in the top-k hits. Preserve this definition for every arm. A refusal phrase or valid citation ID alone does not establish meaning or support.
- **C3:** Cosine ≤0.90 is a declared leakage heuristic, not proof of independence. No minimum tuning win-rate or improvement margin is imposed. Preserve the judge identity, wins, losses, ties and denominator as well as numeric metrics.
- **C4:** Save a standalone D4.1–D4.4 checkpoint without calling `analyze_product()`. Compare at least two compressed **trained-Analyst** arms; half precision supplies the footprint denominator. Re-score the original Stage 3 reference under the same frozen protocol. A failed experiment can show competency, but its failed candidate is not ready to deploy.
- **C5:** Run the combined Stage 4 evaluation only after real integration. A clearly labeled feasible reference fallback can demonstrate integration if compression fails. Submit the written walkthrough; separately issued exam evidence may replace equivalent parts. No paid hosting or separate recording is required.

Use [the reviewer guide](assessment/REVIEWER_GUIDE.md) to apply these judgments and [the submission checklist](docs/SUBMISSION.md) to assemble evidence. Automated checks validate structure and calculations; they do not award Met.
