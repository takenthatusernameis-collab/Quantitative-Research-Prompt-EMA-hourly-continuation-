# Initial task for next agent — EMA hourly continuation universe-refresh gate

**Handoff time:** 2026-11-21T10:39Z (UTC). Bound: `2026-11-22T03:13:02.267371+00:00`.
Gate is **NOT ELIGIBLE** (~16h34m remaining at handoff). State `AWAITING_NEW_ELIGIBLE_CANDIDATES`.

Canonical handoff: `NEXT_AGENT_TASK.md` (top summary + §2d session log + §4 gate-check log).
Pointer only: `TASK_FOR_NEXT_AGENT.md`.

## Your single measurable task

1. **Offline first.** Read this file, `NEXT_AGENT_TASK.md` §3/§4, and `universe/last_scan.json`.
   Recompute eligibility with `scripts/refresh_gate.py:gate_status(state)` (note: it takes the
   parsed `universe/last_scan.json` state as its argument) against independent UTC
   (`date -u`, `datetime.now(timezone.utc)`). Never guess.
2. **If NOT eligible (expected until 2026-11-22T03:13:02Z):** make **no provider calls**.
   Append exactly **one** gate-check row to `NEXT_AGENT_TASK.md` §4 (now / bound / remaining /
   outcome, with real environment status), refresh this file's handoff time/state, then stop.
   Repeated activations inside the same bound stay strictly offline — one row each, nothing else.
   Do **not** schedule wakeups (`cron_list` must stay empty). Do not invent filler work.
3. **If eligible:** run **exactly one** pass
   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`).
   Record snapshot id, coverage (must reach below the floor), floor,
   `eligible_unseen_below_floor_count`, and the new bound.
4. **If that pass yields a batch** (`EXPANSION_AVAILABLE`): apply it through the repo's own cycle —
   `refresh_universe.py fetch` (or `fetch_mcap_snapshot.py --apply`), then `fixtures`, `grid`,
   `state`, `log` — new symbols only, full 66-pair grid, ascending compute but descending market
   cap. Acceptance: `completed_cells == universe_n * 66`. Requires pandas installed.
5. **Never:** rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles
   unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market
   evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and
   `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling;
   follow the AGENTS.md adaptive gate policy.

## Current state (verified 2026-11-21T10:39Z)

- `universe/last_scan.json`: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot
  `mcap_snapshot_20261121_031302` (scanned_at 2026-11-21T03:13:02.267371Z, 25/25 pages,
  2500 entries, lowest rank 2500 / $1,348,381, coverage reaches below floor),
  `universe_n=280`, expansion floor HTR/USDT $1,403,310, `eligible_unseen_below_floor_count=0`,
  `batch_selected=["HTR/USDT"]` (already applied), `next_eligible_refresh_at=2026-11-22T03:13:02.267371+00:00`.
- Universe/grid verified: `universe_n=280`, `symbols_without_fixture=[]`,
  `symbols_without_grid_cells=[]`; grid `results/20261019_135940_grid/progress.json`
  `completed_cells=18480`, `n_symbols=280`, `all_symbols_processed=true`, `next_cell=null`,
  `stopped=false` (18480 == 280×66). `data/fixtures` 283 files incl. `HTR_USDT.csv`;
  `universe/mcap_rank.json` n_symbols=280. `results/FINAL_DECISION.md` preserved. Git tree clean.
- Environment: `python3` 3.12.3 with `pandas 3.1.1`, `numpy 2.5.5`, `pytest 9.2.0`,
  `requests 2.31.0` all importable. The gate check is stdlib-only and needs no install.