# Stable interfaces and artifacts

| Interface | Input | Output |
|---|---|---|
| `inspect(image)` | Real RGB PIL image | Dict with `verdict` GOOD/DEFECTIVE, `defect_type` string/null and `description` string; malformed replies have documented handling |
| `retrieve(query, k=4)` | Nonempty query, positive integer k | At most k actual hits with `source`, `text`, `kind`, `score` |
| `rag_answer(question, k=4)` | Question | `(answer_text, actual_hits_used)` |
| `make_input(note, evidence)` | Prose note and evidence string | Exact training input string |
| `analyst_report(note, evidence)` | Same two strings | Report string from the learner-trained Analyst |
| `analyst_report_compressed(note, evidence)` | Same two strings | Report from the explicitly selected evaluated arm or labeled feasible fallback |
| `analyze_product(image)` | Real image | Dict containing `note` (dict), `evidence` (str), `report` (str); GOOD skips retrieval/Analyst |

The report contains `## ROOT CAUSE ANALYSIS` and **Product**, **Defect**, **Severity**, **Evidence**, **Probable cause**, **Recommended action** fields. Severity is exactly LOW, MEDIUM or HIGH. A passing format check does not establish factual support.

Do not pass a Python dict's string representation where training used a prose note. Retain product identity and qualifiers when constructing a retrieval query. Save intermediate hits for traceability even when the final contract returns an evidence string.

`freeze_record()` records content identity and refuses an overwrite. Its local timestamp is not independent proof of chronology: keep dated notebook snapshots/version history. `record_metrics()` retains a latest summary and an append-only history; full generations, training logs and judgments still belong in separate experiment records.

The four `CAPSTONE_DOCS` retain their exact IDs and text. Chunking may create multiple hits from one source; gold labels refer to source IDs. The source-level all-required-sources metric uses sets, so duplicate chunks do not count as new evidence.
