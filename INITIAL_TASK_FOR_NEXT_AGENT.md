# Initial Task For Next Agent

Read `NEXT_AGENT_TASK.md` first.

## Situation
Gate bound 2026-10-29T21:24:11.948264+00:00 has NOT elapsed (re-verified 2026-10-29T07:15:17Z: eligible=False, ~14h9m remaining via `scripts.refresh_gate.gate_status`). Do NOT contact the provider before the bound. A single resume wakeup (wku_18644a6b2001tKcU6d6A3PdIWy) is set for 2026-10-29T21:29:00Z — let it fire; do NOT duplicate or reschedule it.

## On wakeup (at/after bound)
1. Check gate offline: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`. If not eligible, stop (no provider); re-set wakeup per interval policy.
2. If eligible: run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`.
3. Recompute floor from fresh snapshot; inspect band strictly below floor for eligible unseen candidates.
4. If count==0: record pass, set next bound, re-set wakeup, stop.
5. If count>0: expand per PROMPT.md §2.1 and run full 66-pair grid on each new symbol.
6. Update both handoffs with evidence (snapshot_id, counts, results paths) and preserve negative/blocked results.

## Hard constraints
No provider before bound; one pass max per cycle; no GitHub Actions; no new candle data; no changes to baseline grid/costs/fills/entry-exit; preserve negative/blocked results.
