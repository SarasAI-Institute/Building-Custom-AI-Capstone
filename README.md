# 🏭 RiskLens — Your Capstone Project

**Build a multi-modal product-risk pipeline, one stage per week, and prove every stage with
real numbers.** This is the graded project of *Build Custom AI* — worth **100 points
(25 per week), Satisfactory ≥ 70**.

```
photo ──▶ STAGE 1 · VLM inspector ──▶ defect note (JSON)
                                          │
reviews+specs ──▶ STAGE 2 · RAG ──▶ evidence (cited)
                                          │
                              STAGE 3 · Analyst SLM (QLoRA)
                                          │
                              STAGE 4 · compressed + shipped
                                          ▼
                          root-cause risk report + eval appendix
```

## The premise

You've joined the (fictional) RiskLens team and inherited a **partially working pipeline**:
the plumbing runs, but the intelligence is weak or missing. The baseline inspector ships with
three planted bugs. The baseline retriever is naive. The Analyst doesn't exist yet.
Each week, right after the live session teaches you the technique, you replace one stage with
your own build — and **prove it's better on a frozen evaluation set**.

## Getting started (Week 1, ~5 minutes)

1. Open [`capstone_starter.ipynb`](capstone_starter.ipynb) → **save a copy** to your own
   Colab/Kaggle/Drive. This copy is your project for the next five weeks.
2. Set `TEAM` in the first cell. Switch the runtime to **GPU (T4)**.
3. Read **Section 0** top to bottom — the given infrastructure is your standard library
   *and* the code standard your own work is expected to match.
4. Submit the **share link** (viewable, with saved outputs) — the same link, every week.

## What you deliver each week

| Week | Stage | Headline deliverables | Pts |
|---|---|---|---|
| 1 | 🔍 VLM Inspector | fix 3 planted bugs · beat the baseline on defect F1 on a frozen ≥40-image split · resolution-budget experiment | 25 |
| 2 | 📚 RAG Engine | ≥100-review corpus + gold question set (authored *first*) · beat the naive retriever on recall@4 · refusal stress test · one measured retrieval upgrade | 25 |
| 3 | 🧠 Fine-Tuned Analyst | ≥150 teacher-generated pairs with a full dataset card · QLoRA fine-tune · three-way eval · one training ablation | 25 |
| 4 | 🚀 Ship It | quantization with a pre-committed quality gate · the assembled pipeline · serving economics · 10-product stress test | 25 |
| 5 | 🎓 Final delivery | clean run-all with the five-week metrics ledger · ≤300-word reflection | — |

Every deliverable is labeled **D1.1 … D4.7** in the notebook, with a matching checklist in
[`RUBRICS.md`](RUBRICS.md) — the full criteria, automatic deductions, and up to **+7 bonus
points** (deployed demo, GGUF actually served, second product category, DPO/distillation
experiment).

## Week 5 — final delivery

One clean `Run all`, every `📊 EVALUATION` cell's output saved, `show_ledger()` displaying
your five-week evidence trail, and a ≤300-word reflection: architecture trade-offs, the
number you trust most and least, and what you'd build next.

## The rules

1. **Don't restructure the notebook.** Graders navigate by the section headers and `Dx.y`
   labels. Fill the scaffolds; add cells below them freely; never edit `⚙️ GIVEN` cells.
2. **Frozen means frozen.** Splits, gold sets, dataset cards and gate thresholds are authored
   *above* your build work — cell order is your evidence you didn't peek.
3. **Run all before submitting.** Grading is a manual review of your saved outputs — an
   `📊 EVALUATION` cell with no output is a deliverable that didn't happen. Write your
   training cell as *train-or-load* so run-all doesn't retrain.
4. **Mind the memory budget (16 GB T4):** the VLM stays loaded all session — keep your
   Analyst ≤1.5B and your shipped arm in 4-bit.
5. **Honesty outscores numbers.** An honest 78% with clean methodology beats a suspicious
   95% — the rubric explicitly deducts for eval smells and pays for stated caveats.

## Files

| File | What it is |
|---|---|
| [`capstone_starter.ipynb`](capstone_starter.ipynb) | your project — copy it once, grow it for five weeks |
| [`RUBRICS.md`](RUBRICS.md) | exactly how the 100 points are earned, week by week |

*Questions? Bring them to the live session or the course forum. Good luck — build something
you'd be proud to demo.* 🚀
