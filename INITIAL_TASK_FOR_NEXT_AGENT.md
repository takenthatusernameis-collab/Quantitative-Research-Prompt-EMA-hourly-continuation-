# Initial task for next agent (2026-10-30T04:08:09Z)

You are resuming the EMA hourly continuation. Follow `NEXT_AGENT_TASK.md` exactly.

## State
- Gate: NOT eligible (bound 2026-10-30T22:20:37.246523+00:00, now 2026-10-30T04:08:09Z). ~18h 12m remaining.
- Wakeup: `wku_18afb3da4001GxWH7iH4QEt4cP` due 2026-10-30T22:25:00Z (fires after bound).
- Universe: N=275 unchanged. Snapshot `universe/mcap_snapshot_20261029_222037.json`. `eligible_unseen_below_floor_count=0`, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`.
- Grids: all three complete, 0 blocked. Children `C_stricter_trend` and `C_min_risk_atr` NOT_PROMOTED; baseline 0 credible candidates.

## Do this first (at/after bound)
1. Re-check gate offline:
```bash
PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"
```
2. If not eligible: do NOT call provider. Set a single wakeup just after new bound and stop.
3. If eligible: run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`. Recompute expansion floor. Inspect band strictly below floor for `eligible_unseen_below_floor_count`. If 0: record pass, set `next_eligible_refresh_at`, set single wakeup just after bound, stop. If >0: expand per PROMPT.md §2.1, run full 66-pair grid on each new symbol via `scripts/run_grid.py`, re-aggregate.

## Hard constraints
- Historical research only. No orders/live/paper trading.
- No provider before bound. Max 1 pass/cycle.
- No new candle fetches. Do not modify baseline grid/costs/fills/entry-exit.
- No GitHub Actions trigger/cancel/rerun; no workflow edits.
- Single wakeup only.
- Keep strict confirmatory separate from exploratory.
- Preserve all negative/blocked results. Do not promote without auditable net-of-cost results/provenance/checks.
