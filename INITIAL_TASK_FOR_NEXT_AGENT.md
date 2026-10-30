# Initial Task For Next Agent

## Context (from durable handoff)
- Handoff: NEXT_AGENT_TASK.md (updated 2026-10-30T17:39:20.432514Z)
- Gate: NOT eligible (bound 2026-10-30T22:20:37.246523+00:00, now 2026-10-30T17:39:20.433413+00:00, ~4h 42m remaining). Offline check only; no provider call.
- Single wakeup due 2026-10-30T22:26:00Z (after bound). Do not create a second wakeup; let this one fire.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES, snapshot universe/mcap_snapshot_20261029_222037.json, eligible_unseen_below_floor_count=0, N=275 unchanged.
- Grids: 20261019_135940_grid (baseline), 20261021_172619_grid (C_min_risk_atr), 20261022_134500_grid (C_stricter_trend) all complete (18,150 cells). No credible baseline candidates.
- Working tree clean (`git status --short` empty).

## Exact task to complete now

Nothing is actionable before `2026-10-30T22:20:37.246523+00:00`. Wait for the scheduled wakeup (due 2026-10-30T22:26:00Z, after the bound).

When it fires, at/after the bound, re-run the offline gate check:

```bash
PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"
```

- If still not eligible: stop (bound has not meaningfully elapsed / gate still closed). Do NOT call the provider. Do NOT create a second wakeup. Update NEXT_AGENT_TASK.md and INITIAL_TASK_FOR_NEXT_AGENT.md with the unchanged bound and re-set a single wakeup just after it.
- If eligible: run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`, recompute the expansion floor, inspect the band strictly below the floor for `eligible_unseen_below_floor_count`. If 0: record the pass, set `next_eligible_refresh_at`, re-set the wakeup just after the new bound (cancel the existing one first), stop. If >0: expand per PROMPT.md §2.1 and run the full 66-pair grid on each new symbol via `scripts/run_grid.py`, then re-aggregate.

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

The only actionable step before the bound is to confirm offline gate status and do nothing until/after 2026-10-30T22:20:37.246523+00:00. After the bound, run the gate check and follow the branch above.

(End of file - total 38 lines)