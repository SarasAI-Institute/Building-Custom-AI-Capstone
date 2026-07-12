# 🏭 RiskLens — Multi-Modal Product-Risk Pipeline (Capstone)

**The graded project of Build Custom AI** — **100 points, 25 per week, Satisfactory ≥ 70** —
one notebook that grows for five weeks and ends as a working system: a VLM spots visual
defects → RAG gathers evidence from reviews + specs → a fine-tuned, quantized Analyst SLM
writes the root-cause risk report.

This mirrors the 10xCoding/PromptLab format (inherit a partially-working project → fix its
bugs → extend it weekly → final delivery), translated to notebooks: students inherit **working
plumbing plus deliberately weak baselines**, and each week replace one stage's baseline with
their own build — proving the improvement on a frozen set.

## How it works

1. **Week 1, students copy `capstone_starter.ipynb`** to Colab/Kaggle/their GPU box and submit
   the **share link**. The link never changes — every week they improve the same notebook.
2. The notebook is a real project skeleton:
   - **`⚙️ GIVEN` infrastructure** — VLM plumbing (`ask_vlm`), embedding/index helpers,
     format checker, benchmarker, data loaders, the metrics ledger (`record_metrics()` →
     `capstone_metrics.json`). Boilerplate is provided; intelligence is the work.
   - **Baselines to beat** — `inspect_v0` ships with 3 documented bugs (the PromptLab
     "fix the backend bugs" move); `retrieve_v0` is a naive retriever — the rubric requires
     the student's version to beat them measurably.
   - **Lettered deliverables** (D1.1–D4.7) with per-week checklists that map 1:1 to the rubric.
   - **Frozen-artifact cells above workspaces** (split / gold set / dataset card / gate) —
     cell order is grading evidence.
   - **`📊 EVALUATION` cell per stage** — computes the stage's metrics (F1 vs baseline, recall
     tables, gate verdict) and logs them to the ledger. Grading is manual — the former
     enforcement asserts remain as comments, documenting the rubric minimums (≥40 test images,
     ≥20 gold questions, ≥150 teacher pairs, leakage ≤0.90…).
3. **Grading:** each week from the submitted link with saved outputs — see [`RUBRICS.md`](RUBRICS.md):
   25 pts/week in PromptLab style (criteria tables, automatic deductions, up to +10 bonus).
4. **Week 5 (no new points, deductions if skipped):** run top-to-bottom, then the **hidden
   holdout** — a `⚙️ GIVEN` builder cell assembles `predictions.json` from the student's own
   contracts over the released `student_facing/` inputs (see `../course_setup/`), max 3
   submissions to the scoring Space, scorecard pasted into the notebook.

## Files

| File | What it is |
|---|---|
| `capstone_starter.ipynb` | the notebook students copy in Week 1 and grow all course |
| `capstone_solution.ipynb` | **INSTRUCTOR ONLY — never publish.** Full reference implementation of D1.1–D4.7: the grading reference and the end-to-end system test |
| `RUBRICS.md` | weekly 100-pt rubrics + final, with grader quick-procedure |

## Why this design

- **Inherit → fix → extend** — the PromptLab arc in notebook form: given plumbing, buggy
  baselines to diagnose (Week 1's three inspector bugs), naive baselines to beat measurably
  (Week 2's retriever), then build-from-scratch weeks (3–4) once the discipline is set.
- **Contracts between stages** mean Week 2 can proceed even if Week 1 was weak (stages compose
  through interfaces, not through each other's internals) — and the Week-5 holdout builder
  runs against those same contracts unchanged.
- **`record_metrics()` ledger** makes five weeks of eval history visible in one place —
  regressions (e.g. after compression) become explainable rather than hidden.
- **Cell-order-as-evidence + grading-cell asserts** let graders verify eval discipline and
  minimums without re-running anything.
- **Process over leaderboard**: the rubric pays for honest evaluation; the hidden holdout
  catches overfitting anyway (disjoint vocabulary, unseen categories, max 3 submissions).

## Instructor setup checklist

- [ ] Host the holdout + scoring Space (`../course_setup/README.md`, Option A).
- [ ] Share the `student_facing/` inputs at the start of Week 5 (not earlier).
- [ ] Announce the submission form (notebook link + team name) in Week 1.
- [ ] Remind students weekly: run all, save outputs, grading cells exactly once.
