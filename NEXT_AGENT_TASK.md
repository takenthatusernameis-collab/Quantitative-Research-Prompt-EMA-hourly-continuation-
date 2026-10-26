# NEXT AGENT TASK — Durable Handoff

## Turn 2026-10-26T18:30Z (gate check — not yet eligible, no provider contact)
- Offline gate check (run at `2026-10-26T18:38:57.318320+00:00`): `eligible=False`, bound `2026-10-27T17:19:35.198212+00:00` not yet elapsed. Reason: `the 24 h refresh bound 2026-10-27T17:19:35.198212+00:00 has not elapsed yet`.
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261026_171935`, N=275, floor ALPINE/USDT $3,426,968, eligible_unseen_below_floor_count 0).
- Baseline grid `results/20261019_135940_grid` complete (18150 cells = 275 x 66, 0 blocked/credible). Child mutation grid `results/20261021_172619_grid` complete and evaluated (not promoted).
- `git status --short` empty, `git diff --stat` empty. No code changes.
- Wakeup scheduled (`wku_17982f35900158vDyzPuEp3Tog`) to resume at `2026-10-27T17:39:47.540Z` (after bound).

**Current state:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Universe N=275, baseline grid complete. Gate bound `2026-10-27T17:19:35.198212+00:00` not yet elapsed. No provider contact permitted before the bound. Nothing actionable until bound elapses.

**Next action:** wait for bound (wakeup scheduled), then check eligibility offline first:
```bash
PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
```
Must return `eligible: True`. If `False`, stop and report the bound — nothing actionable. If eligible, run exactly one 20-page ranking pass (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`), re-check `eligible_unseen_below_floor_count`, expand or record pass and set next +24 h bound, then update both handoff files.

**Hard constraints:** no provider call before bound; no second writer on baseline grid; no partial-grid promotion; no changes to costs/folds/entry-exit/gates; do not combine variables; do not stop on failures — expand descending market cap and continue; ignore pre-existing clock bug in `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`.

**Evidence to report:** gate status before/after; snapshot path/pages/floor/N and eligible count; if expanded old→new N/ranks/log entry; if not log entry + new bound; grid/aggregate/candidate paths and blocked/credible counts; tests after changes (or confirm unchanged if none).
