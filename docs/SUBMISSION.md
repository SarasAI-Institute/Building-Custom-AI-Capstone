# Five milestones, one continuing notebook

Keep the same shareable notebook link; save outputs, a dated snapshot, completion summary and known issues at each milestone. Preserve artifact access from the reviewer's context. Administrative dates and attempts follow course policy.

| Milestone | Required evidence | Freeze first |
|---|---|---|
| Module 1 | D1.1–D1.7; ≥40 test images/≥20 per class; three prompt iterations including few-shot; baseline/final defect F1; error analysis; three image sizes, time and price assumptions | Image membership + separate development set before prompt iteration |
| Module 2 | D2.1–D2.7; ≥100 real reviews + four unchanged official docs + two authored linked docs; ≥20 gold/three multi-hop; recall@1,2,4,8; actual citations; five unsupported questions/four meaningful refusals; two judge axes; measured upgrade and graph design note | Gold before indexing; unsupported questions before testing refusals |
| Module 3 | D3.1–D3.7; ≥150 raw real-teacher pairs; complete card and cleaning counts; ≥25 frozen tests/max cosine ≤0.90; real trained/reloaded adapter; format/content/blind A/B; one-variable retrained ablation | Test membership and dataset card before training |
| Module 4 | D4.1–D4.4; technique note; two compressed trained-model arms; same-row quality comparisons; half-precision footprints; actual token throughput/p50/p95/cost; gate-respecting decision | Gate, units, reference, candidates, intended arm and price before re-scoring |
| Module 5 | D4.5–D4.7; real integration; three demos (one good/two defective); ≥10 full-pipeline products/stage times/failure taxonomy; deployment note; saved weights/load path; ledger; ≤300-word reflection; written walkthrough | Selected artifact identity and batch plan before final run |

## Final run/load

Restore the data and saved adapter/checkpoint in a clean runtime. Run setup and completed workspaces top to bottom. Delivery must load the recorded weights rather than unexpectedly repeat training or teacher generation. Preserve the source and artifact versions used. Save all evaluation outputs and full comparison records, plus `capstone_metrics.json` and its JSONL history.

The starter deliberately contains unimplemented learner tasks. It is not a completed solution and is expected to stop at an unfinished task. Do not replace these with fabricated outputs to make Run all green.

## Written walkthrough

Explain one actual component and why it fits RiskLens; state what would fail if a named part were removed. Trace one demonstrated product, defend one reported metric and discuss a failed experiment or unsupported claim using saved evidence. The ≤300-word reflection is a separate requirement.
