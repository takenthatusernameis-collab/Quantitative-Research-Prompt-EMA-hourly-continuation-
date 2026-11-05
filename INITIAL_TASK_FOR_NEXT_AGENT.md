# Initial task for next agent

Time: 2026-11-05T05:25:46Z

## Handoff read (completed)
- Read `NEXT_AGENT_TASK.md` (new entry appended this turn) and `INITIAL_TASK_FOR_NEXT_AGENT.md` (prior).
- Gate state from `universe/last_scan.json` (unchanged): `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261105_034137` scanned at `2026-11-05T03:41:37.153817+00:00`, `next_eligible_refresh_at=2026-11-06T03:41:37.153817+00:00`, expansion floor `PIXEL/USDT ($3,351,513)`, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`, universe_n=275.
- Gate check (this turn): NOT eligible (~22h15m remaining), re-derived independently via inline Python. Wakeup scheduled for this session `wku_1aa2d4a180016y82cS3RKM5YWy` due `2026-11-06T03:46:56Z` (5 min after gate opens); do not duplicate.

## What to do next
1. **Do not apply anything.** Batch is empty; SUKU still has no fixture/grid coverage. Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` records program-level rejection.
2. **Wait for gate eligibility.** At/after `2026-11-06T03:41:37.153817+00:00`, re-check with `scripts.refresh_gate.gate_status` and run `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20` to get a fresh snapshot, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage. If eligible with candidates, follow `AGENTS.md`/README constraints strictly (historical research only, no live/paper trading, preserve signal/cost assumptions, document provenance/selection/survivorship). If still no candidates, update `universe/last_scan.json` via refresh flow and set a new wakeup ~5 min after next `next_eligible_refresh_at`.
3. **Preserve history.** Append timestamped gate re-check to `NEXT_AGENT_TASK.md` before ending. Keep clean git state (`git status --short` empty). Do not modify unrelated projects or trigger paid services.

## Constraints
- Historical research only; no orders/deploys.
- Preserve EMA signal/fill/cost assumptions.
- If blocked/unavailable, follow adaptive policy: exploratory only if explicitly versioned/labeled, never treat current snapshot as confirmatory history.
- Do not silently relax frozen history/sample/execution/cost requirements; relaxed versions need new ID with survivorship/selection/uncertainty/cost sensitivity.
- Append to `NEXT_AGENT_TASK.md` on each gate re-check; update this file for the following agent.