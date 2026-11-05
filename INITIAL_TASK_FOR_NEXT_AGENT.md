# Initial task for next agent

Time: 2026-11-05T05:16:00Z

## Handoff read (completed)
- Read `NEXT_AGENT_TASK.md` (latest entry) and `INITIAL_TASK_FOR_NEXT_AGENT.md` (prior).
- Gate state from `universe/last_scan.json` (unchanged): `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261105_034137` scanned at `2026-11-05T03:41:37.153817+00:00`, `next_eligible_refresh_at=2026-11-06T03:41:37.153817+00:00`, expansion floor `PIXEL/USDT ($3,351,513)`, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`, universe_n=275.
- Gate check: not eligible (~22h25m remaining). No pending wakeups in this session.

## What to do next
1. **Do not apply anything.** Batch is empty; SUKU still has no fixture/grid coverage. Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` records program-level rejection.
2. **Wait for gate eligibility.** At/after `2026-11-06T03:41:37.153817+00:00` (gate opens), re-check with `scripts.refresh_gate.gate_status` and run `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20` to get fresh snapshot, then `--apply-from` as appropriate. If eligible with candidates, follow `AGENTS.md`/README constraints strictly (no live/paper trading, preserve signal/cost assumptions, document provenance/selection). If still no candidates, update `universe/last_scan.json` via the refresh flow and set a new wakeup ~5 min after next `next_eligible_refresh_at`.
3. **Preserve history.** If no actionable expansion appears again, do not force changes. Keep clean git state and update `NEXT_AGENT_TASK.md` with a timestamped gate re-check before ending.

## Constraints
- Historical research only; no orders/deploys.
- Do not modify unrelated projects or trigger paid services.
- Preserve EMA signal/fill/cost assumptions.
- If blocked/unavailable, follow adaptive policy: exploratory only if explicitly versioned/labeled, never treat current snapshot as confirmatory history.
- Append to `NEXT_AGENT_TASK.md` on each gate re-check; update this file for the following agent.
