# Initial Task For Next Agent

## Context (from durable handoff)
- Handoff: NEXT_AGENT_TASK.md (updated 2026-10-30T16:01:53Z)
- Gate: NOT eligible (bound 2026-10-30T22:20:37.246523+00:00, now 2026-10-30T16:01:53Z, ~6h 19m remaining). Offline check only; no provider call.
- Durable single wakeup: wku_18d4fdd9b0015rux3kPqCVO2FR due 2026-10-30T22:28:00Z (after bound). Do not create a second wakeup.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES, snapshot universe/mcap_snapshot_20261029_222037.json, eligible_unseen_below_floor_count=0, N=275 unchanged.
- Grids: 20261019_135940_grid (baseline), 20261021_172619_grid (C_min_risk_atr), 20261022_134500_grid (C_stricter_trend) all complete (18,150 cells). No credible baseline candidates.

## Exact task to complete now

At/after 2026-10-30T22:20:37.246523+00:00, re-run the offline gate check:

```bash
PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"
```

If still not eligible: stop (wakeup already set after bound). Do NOT call provider, do NOT create second wakeup.
If eligible: run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`, recompute expansion floor, inspect band strictly below floor for `eligible_unseen_below_floor_count`. If 0: record pass, set `next_eligible_refresh_at`, re-set wakeup just after new bound (cancel existing first), stop. If >0: expand per PROMPT.md §2.1 and run full 66-pair grid on each new symbol via `scripts/run_grid.py`, then re-aggregate.

## Hard constraints
- Historical research only; no orders/live/paper trading.
- No provider before bound.
- 1 pass max/cycle.
- Do not fetch new candle data; do not modify baseline grid/costs/fills/entry-exit semantics.
- Do not trigger/cancel/rerun GitHub Actions or edit workflows.
- Single wakeup only.
- Keep strict confirmatory separate from exploratory.
- Preserve all negative/blocked results; do not select winner on holdout/claim profitability without auditable net-of-cost, provenance, independent checks.

## Measurable next task

Same as the exact task above: the only actionable step before the bound is to confirm offline gate status and do nothing until/after 2026-10-30T22:20:37.246523+00:00.
