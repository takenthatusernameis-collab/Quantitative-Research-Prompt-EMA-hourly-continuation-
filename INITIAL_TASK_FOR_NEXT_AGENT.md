# Initial Task For Next Agent

Read `NEXT_AGENT_TASK.md` first.

Gate bound 2026-10-29T21:24:11.948264+00:00 NOT elapsed (verified 2026-10-29T04:33:41Z: eligible=False, ~17h remaining). Do NOT contact provider before bound. Wakeup **wku_185efb1aa001dX8sVwZ62RxP8N** due 2026-10-29T21:29:00.000Z is set — let it fire; do NOT duplicate or reschedule it.

On wakeup (at/after bound):
1. Check gate offline: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`. If not eligible, stop (no provider); re-set wakeup per interval policy.
2. If eligible: run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`.
3. Recompute floor from fresh snapshot; inspect band strictly below floor for eligible unseen candidates.
4. If count==0: record pass, set next bound, re-set wakeup, stop.
5. If count>0: expand per PROMPT.md §2.1 and run full 66-pair grid on each new symbol.
6. Update both handoffs with evidence (snapshot_id, counts, results paths) and preserve negative/blocked results.

Hard constraints: no provider before bound; one pass max per cycle; no GitHub Actions; no new candle data; no changes to baseline grid/costs/fills/entry-exit; preserve negative/blocked results.