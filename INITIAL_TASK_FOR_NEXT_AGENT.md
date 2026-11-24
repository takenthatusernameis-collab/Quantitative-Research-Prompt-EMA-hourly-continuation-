# Initial Task for Next Agent — EMA Hourly Continuation Universe-Refresh Gate

**Handoff time:** 2026-11-24T10:48Z (offline gate check completed; one gate-check row appended to `NEXT_AGENT_TASK.md` §4)

## Current State (verified this session)

- **Gate status:** NOT ELIGIBLE — bound `2026-11-24T14:01:08.626759+00:00` has not elapsed (~3h12m26s / 11,546s remaining)
- **State:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- **Last snapshot:** `mcap_snapshot_20261123_140108` (25/25 pages, 2500 entries, lowest rank 2500 / $1,374,604, `coverage_reaches_below_floor=true`)
- **Expansion floor:** NUM/USDT $1,385,628
- **Eligible unseen below floor:** 0
- **Batch pending:** none

## Universe/Grid Verification (offline, all checks passed)

- `universe_n=281` symbols in `universe/mcap_rank.json`
- Grid: `results/20261019_135940_grid/progress.json` → `completed_cells=18546`, `n_symbols=281`, `all_symbols_processed=true`, `next_cell=null`, `stopped=false` (18546 == 281×66)
- Fixtures: 284 files in `data/fixtures/` (283 CSV + `fetch_manifest.json`), incl. `AZERO_USDT.csv`
- `results/FINAL_DECISION.md` preserved
- Git tree clean (`git status --short` empty, `git diff --stat` empty)

## Environment

- Python 3.12.3 + requests 2.31.0 only
- pandas/numpy/pytest NOT importable (`ModuleNotFoundError`; temp home wiped again)
- Gate tooling is stdlib-only and ran OK

## Your Task (one measurable task)

1. **Offline first:** read `NEXT_AGENT_TASK.md` and `universe/last_scan.json`. Recompute eligibility from `next_eligible_refresh_at` (`2026-11-24T14:01:08.626759+00:00`) with `scripts/refresh_gate.py:gate_status` vs independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess.

2. **If NOT eligible (expected until 2026-11-24T14:01:08Z):** make **no provider calls**. Append exactly one gate-check row to the log in `NEXT_AGENT_TASK.md`, then stop. Do not schedule wakeups. Repeated activations inside the same bound stay strictly offline (no provider call, no fixture/candle fetch, no grid rerun, no apply); each activation records exactly one row and nothing else.

3. **If eligible:** run **exactly one** pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`; provider calls allowed only after the bound). Record snapshot id, coverage (must reach below the floor), floor, `eligible_unseen_below_floor_count`, new bound.

4. **If that pass yields a batch** (`EXPANSION_AVAILABLE`): apply it through the repo's own cycle — `refresh_universe.py fetch` (or `fetch_mcap_snapshot.py --apply`), then `fixtures`, `grid`, `state`, `log` — new symbols only, full 66-pair grid, ascending compute but descending market cap; acceptance is `completed_cells == universe_n * 66`. Requires pandas installed (reinstall with `pip install --user pandas numpy pytest` if missing).

5. **Never:** rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow the AGENTS.md adaptive gate policy.

## Key Files to Read

- `NEXT_AGENT_TASK.md` (this handoff log, updated with your check)
- `universe/last_scan.json` (current gate state)
- `AGENTS.md` / `README.md` / `PROMPT.md` (protocol reference)

## Gate-Check Log Entry Template

Add a row to the table in `NEXT_AGENT_TASK.md` §4:

| UTC now | Bound | Remaining | Outcome |
| --- | --- | --- | --- |
| 2026-11-24T01:25:15.529240+00:00 | 2026-11-24T14:01:08.626759+00:00 | ~12h35m47s (45,347s) | NOT ELIGIBLE; [your verification summary] |

---

**No provider calls were made this session. No wakeups scheduled. The next agent should perform only an offline gate check unless the 24-hour bound has elapsed.**