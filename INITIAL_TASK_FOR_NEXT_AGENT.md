# Initial Task For Next Agent

Read `NEXT_AGENT_TASK.md` first.

Gate bound 2026-10-29T21:24:11.948264+00:00 NOT elapsed (verified 2026-10-29T01:22:51Z: eligible=False, reason="the 24 h refresh bound ... has not elapsed yet"). Do NOT contact provider before bound. Resume wakeup wku_1854019a7001eMyiUzafmTDAOy due 21:21:48Z already scheduled — do NOT duplicate.

Steps:
1. Check gate offline: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`. If not eligible, STOP (no provider).
2. If eligible: run one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`.
3. Recompute floor; check eligible count below floor.
4. If 0: record pass, set next bound, re-set wakeup, STOP.
5. If >0: expand per PROMPT.md §2.1 and run full 66-pair grid on each new symbol.
6. Update both handoffs.

Hard constraints: no provider before bound; one pass max; no GitHub Actions; no new candle data; no baseline/cost changes; preserve negative/blocked results.
"