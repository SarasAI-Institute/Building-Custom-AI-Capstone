# Applying the competency rubric

1. Check that the notebook, saved outputs and required artifacts are accessible. Return incomplete delivery for correction before assessment.
2. Review the module's MUST PASS criterion first: C1.1, C2.3, C3.2, C4.2 or C5.1. If Not Yet, explain the gap and stop that module's review. Record the other criteria as not reviewed, not automatically failed.
3. Inspect each remaining criterion against the submitted evidence. Record Met or Not Yet with an evidence location and explanation. A strong metric does not cancel a process failure.
4. Mark the competency Mastered only when all its criteria are Met. Record project mastery only when all five competencies are Mastered.
5. On revision, inspect the Not Yet criteria and any previously Met evidence affected by the change. Keep the prior assessment record.

## Feedback record

Copy [feedback_template.json](feedback_template.json) for each review. `null` means not reviewed. Record actual notebook cells/artifacts, not generic statements. The structure checker checks these records; human reviewers make the judgments.

## Calibration examples

- Excellent F1 with test-driven prompt selection: C1.1 is Not Yet. Explain the versioning/evaluation gap before continuing.
- Four refusal phrases followed by invented warranty answers: phrase matching has not established C2.3.
- Trained model loses the blind comparison, with valid data and complete evidence: do not invent a C3 win-rate threshold.
- Compressed candidate fails its original gate, and the learner preserves the failure and chooses a feasible fallback: this can satisfy C4 when all five criteria have evidence. Do not label the candidate approved.
- A ten-case batch has no observed failures: require that finding and its limits, not fictional failures.
- A polished hosted interface with missing real components: does not satisfy C5.1.

Run `python scripts/check_review.py path/to/review.json` from the repository root to check a copied review record. This validates labels, evidence/feedback fields, must-pass order and completeness. It summarizes the judgments you supplied; it does not inspect or award competency from the learner's artifacts. Preserve each prior review and use a fresh record for reassessment.
