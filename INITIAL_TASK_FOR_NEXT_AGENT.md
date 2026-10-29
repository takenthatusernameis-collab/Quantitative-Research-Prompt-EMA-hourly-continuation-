# Initial Task Message for Next Agent

Gate is not eligible yet (bound 2026-10-29T21:24:11.948264+00:00; now ~14:35:01Z). Wakeup likely exists at ~21:27:15Z; do not create a second wakeup.

At/after bound:
1. Check gate: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`
2. If not eligible -> stop, re-set wakeup. If eligible -> run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`. Recompute floor; if `eligible_unseen_below_floor_count==0` -> record pass, set `next_eligible_refresh_at`, re-set wakeup, stop. If >0 -> expand per PROMPT §2.1, run full 66-pair grid per new symbol via `scripts/run_grid.py`, re-aggregate.

Constraints: historical research only; no orders; no provider before bound; 1 pass max/cycle; no new candle data; no changes to baseline grid/costs/fills/entry-exit; no GH Actions changes; single wakeup; keep confirmatory/exploratory separate.
