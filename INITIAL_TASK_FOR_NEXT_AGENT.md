# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Handoff updated:** 2026-11-18T19:51:52Z. The due 24 h ranking pass was **taken** this session (the previous handoff had deferred it wrongly; see `NEXT_AGENT_TASK.md` §1–§2 for evidence and the full gate-check log).

Read `AGENTS.md`, `README.md`, `PROMPT.md`, `NEXT_AGENT_TASK.md` and `universe/last_scan.json` before acting. Historical research only: no orders, no live/paper deployment, free public data, no-cost tooling.

## Verified state at handoff

- `universe/last_scan.json`: state **`AWAITING_NEW_ELIGIBLE_CANDIDATES`**, snapshot_id `mcap_snapshot_20261118_195023`, `scanned_at=2026-11-18T19:50:23.792771+00:00`, source CoinGecko `/api/v3/coins/markets` (usd, market_cap_desc), 25/25 pages, 2500 entries, `coverage_reaches_below_floor=true`, lowest rank 2500, lowest mcap **$1,484,631**, `history_probe_failures=[]`, `universe_n=278`, expansion floor **CERE/USDT $1,528,741**, `eligible_unseen_below_floor_count=0`, `eligible_unseen_below_floor=[]`, `batch_selected=[]`.
- **Refresh bound (the gate): `2026-11-19T19:50:23.792771+00:00`.** Until then the ranking must not be queried again (PROMPT.md §2.1.5).
- Universe and grid: `PYTHONPATH=. python3 scripts/refresh_universe.py plan` → `universe_n=278`, `symbols_without_fixture=[]`, `symbols_without_grid_cells=[]`; `results/20261019_135940_grid/progress.json` `completed_cells=18348`, `n_symbols=278` (278 × 66, 0 blocked). `universe/mcap_rank.json` unchanged at 278 symbols. `results/FINAL_DECISION.md` preserved (program decision: no credible edge to date; expansion continues).
- **Environment:** python 3.12.3 with `pandas 3.1.1`, `numpy 2.5.5`, `pytest 9.2.0`, `requests 2.31.0`, installed via `pip install --user` under `/home/runner/work/_temp/kilo-home/.local`. That home is temporary: **re-check the imports first**; if they are missing, run `python3 -m pip install --user pandas numpy pytest` before any grid/signal/pytest work. Gate/scan tooling is stdlib-only.

## Your task (one measurable item)

1. **Offline first.** Run `PYTHONPATH=. python3 scripts/refresh_universe.py plan` and recompute the gate with `scripts/refresh_gate.py:gate_status` against `next_eligible_refresh_at` (`2026-11-19T19:50:23.792771+00:00`) and independent UTC (`date -u`, `datetime.now(timezone.utc)`). Never guess.
2. **If the gate is NOT eligible (expected):** make **no provider calls**. Append exactly one gate-check row (now / bound / remaining / state `AWAITING_NEW_ELIGIBLE_CANDIDATES` / 0 eligible unseen / grid 278–18348 / real env status) to the table in `NEXT_AGENT_TASK.md` §4, then stop. Keep `cron_list` empty; do not schedule wakeups.
3. **If the gate IS eligible:** gate eligibility means the pass is **due** — an `AWAITING_NEW_ELIGIBLE_CANDIDATES` state with `eligible_unseen_below_floor_count=0` describes the *old* snapshot and does not cancel the pass. Run **exactly one** `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`; ~15–20 min because pages are spaced for CoinGecko rate limits), then record snapshot id, coverage (must reach below the floor), floor, `eligible_unseen_below_floor_count` and the new bound.
4. **If that pass yields a batch** (`EXPANSION_AVAILABLE`): apply it through the repo's own cycle — `refresh_universe.py fetch` (or `fetch_mcap_snapshot.py --apply`), then `fixtures`, `grid`, `state`, `log`; new symbols only, full 66-pair grid, descending market cap; acceptance `completed_cells == universe_n * 66`.
5. **Never:** rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles unnecessarily, place orders, change the EMA signal / fill / cost assumptions, treat fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative and blocked results and `results/FINAL_DECISION.md`.
