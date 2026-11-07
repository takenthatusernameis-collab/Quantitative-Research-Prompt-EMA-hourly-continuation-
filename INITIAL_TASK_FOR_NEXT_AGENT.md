# Initial task for next agent — EMA hourly continuation

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md` (latest entry is authoritative). Do **not** guess gate state.

## Current gate state (offline re-check 2026-11-07T08:26:28Z)
- **NOT ELIGIBLE** for a new 20-page snapshot pass.
- `now=2026-11-07T08:26:28.145315+00:00`, `next_eligible_refresh_at=2026-11-07T10:16:12.893046+00:00`, `remaining≈6584.75s` (~1h49m45s). Source: `universe/last_scan.json` + independent `datetime.now(timezone.utc)` cross-check.
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261106_101612` (`universe/mcap_snapshot_20261106_101612.json`), scanned `2026-11-06T10:16:12.893046+00:00`, CoinGecko `/api/v3/coins/markets` (usd, market_cap_desc), 20/20 pages/2000 entries, `lowest_rank_covered=2000`, `lowest_market_cap_usd=3179353`, `coverage_reaches_below_floor=true`, `universe_n=275`, floor `{PIXEL/USDT, $3,254,887}`, `eligible_unseen_below_floor_count=0`, `eligible_unseen_below_floor=[]`, `batch_selected=[]`.
- Guards: **`data/fixtures/SUKU_USDT.csv` ABSENT; no `*SUKU*` in tree → `--apply` MUST NOT run** without verified fixture/grid coverage for any selected candidate. Baseline grid `results/20261019_135940_grid/progress.json` complete (`completed_cells=18150, n_symbols=275, n_pairs=66, all_symbols_processed=true, stopped=false, stop_reason=null, next_cell=null`); `results/FINAL_DECISION.md` preserved (program-level rejection).

## Retained wakeup
- `wku_1b3cb2ba10013PChsdJTbjSl1z` due `2026-11-07T10:21:00Z` (~5 min after gate opens). **Do not schedule a duplicate.**

## Your bounded task
1. **Re-verify gate eligibility at start** from `universe/last_scan.json` (independent UTC check). Do not guess.
2. **If still NOT ELIGIBLE (before 2026-11-07T10:16:12.893046+00:00):** make **no provider calls**, no snapshot pass, no `--apply`, no candle fetches, no grid reruns, no EMA/cost/fill changes. Append a short offline re-check record to `NEXT_AGENT_TASK.md` (exact now/bound/remaining + state evidence + guards). Update this file if needed. Stop; rely on the retained wakeup.
3. **If ELIGIBLE (at/after 2026-11-07T10:16:12.893046+00:00):** run **at most one** 20-page snapshot pass: `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`. Recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, and record full evidence in `NEXT_AGENT_TASK.md`. Review any new candidate(s) for fixture/grid coverage **before any `--apply`** — **never apply without verified coverage** (SUKU guard applies to any analogously uncovered name).
4. **Never:** rerun grids, fetch candles, place orders, use fixtures as market evidence, blur confirmatory vs exploratory, or make silent cost/fill/EMA/history changes.

## Constraints
Historical research only; no orders/live/paper trading; free public data/no-cost tooling; preserve negative/blocked results; follow `AGENTS.md` adaptive gate policy.
