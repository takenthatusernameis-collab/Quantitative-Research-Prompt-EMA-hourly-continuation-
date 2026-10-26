# NEXT AGENT TASK — Durable Handoff

## Turn 2026-10-26T20:06Z (gate check — not yet eligible, no provider contact)
- Offline gate check: `eligible=False`, bound `2026-10-27T17:19:35.198212+00:00` not yet elapsed (current time 2026-10-26T20:06:19Z). Reason: `the 24 h refresh bound 2026-10-27T17:19:35.198212+00:00 has not elapsed yet`.
- No provider contact. State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261026_171935`, N=275, floor `ALPINE/USDT` $3,426,968, eligible_unseen_below_floor_count=0.
- Baseline grid `results/20261019_135940_grid` complete (18150 cells, 0 blocked/credible). Child mutation grid complete and evaluated, not promoted.
- `git status --short` empty, `git diff --stat` empty. No code changes.
- Wakeup scheduled to resume after bound (wakeups visible via runtime; if missing, schedule resume at/after bound).

**Current state:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Gate bound not yet elapsed. No provider contact permitted before bound. Nothing actionable until then.

**Next action (after bound):** check eligibility offline first:
```bash
PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
```
Must return `eligible: True`. If `False`, stop and report bound + current `next_eligible_refresh_at`. If eligible, run exactly one 20-page ranking pass (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`), re-check `eligible_unseen_below_floor_count`, expand or record pass and set next +24 h bound, then update both handoff files (`NEXT_AGENT_TASK.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`).

**Hard constraints:** no provider call before bound; no second writer on baseline grid; no partial-grid promotion; no changes to costs/folds/entry-exit/gates; do not combine variables; do not stop on failures — expand descending market cap and continue; ignore pre-existing clock bug in `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`.

**Evidence to report:** gate status before/after; snapshot path/pages/floor/N and eligible count; if expanded old→new N/ranks/log entry; if not log entry + new bound; grid/aggregate/candidate paths and blocked/credible counts; tests after changes (or confirm unchanged if none).
