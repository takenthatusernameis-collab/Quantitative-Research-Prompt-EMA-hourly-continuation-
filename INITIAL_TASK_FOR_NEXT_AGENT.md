# Initial Task For Next Agent

Read `NEXT_AGENT_TASK.md` first.

Gate bound 2026-10-29T21:24:11.948264+00:00 NOT elapsed (verified 2026-10-29T03:22Z: eligible=False, ~18h 02m remaining). Do NOT contact provider before bound. Wakeup set this session: **wku_185af5e44001at3cF6d2tO4E7R** due 2026-10-29T21:26:21Z — let it fire; do NOT duplicate or reschedule.

On wakeup (at/after 2026-10-29T21:24:11.948264+00:00):
1. Check gate offline: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`. If not eligible, STOP (no provider).
2. If eligible: run one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20` only.
3. Recompute floor; check eligible count strictly below floor.
4. If 0: record pass, set next bound, re-set wakeup, STOP.
5. If >0: expand per PROMPT.md §2.1 and run full 66-pair grid on each new symbol.
6. Update both handoffs.

Hard constraints: no provider before bound; one pass max; no GitHub Actions; no new candle data; no baseline/cost changes; preserve negative/blocked results.

(End of file)