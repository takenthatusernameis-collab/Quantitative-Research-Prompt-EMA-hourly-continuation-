# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

## Status at handoff (2026-11-12T01:27:02Z)

Gate state: **AWAITING_NEW_ELIGIBLE_CANDIDATES** — most recent eligible snapshot pass completed 2026-11-12T00:58:05Z with 0 eligible unseen candidates below the expansion floor. **No provider calls** until `next_eligible_refresh_at`.

- `universe/last_scan.json` (re-read, JSON valid): state=`AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261112_005805`, snapshot_path=`universe/mcap_snapshot_20261112_005805.json` (present, 544,098 bytes), scanned_at=`2026-11-12T00:58:05.114706+00:00`, source=CoinGecko public API `/api/v3/coins/markets` (usd, market_cap_desc).
- Coverage: pages 20/20, entries_count=2000, `all_requested_pages_returned=true`, lowest_rank_covered=2000, lowest_market_cap_usd=$3,032,868, `coverage_reaches_below_floor=true`.
- Universe: n=275. Expansion floor (recomputed vs included-universe fixtures): **ZKJ/USDT $3,149,088**. `eligible_unseen_below_floor_count=0`, `batch_selected=[]`, `eligible_unseen_below_floor=[]`.
- Prior batch names DENT/USDT, SUKU/USDT, ESE/USDT are now above floor or absent from top-2000 snapshot in that pass context; fixtures for all three remain **ABSENT** (`data/fixtures/{DENT,SUKU,ESE}_USDT.csv`) and baseline grid coverage **ABSENT** in `results/20261019_135940_grid/progress.json` (275 symbols). No `--apply` was run (nothing to apply). `--apply` remains prohibited for any candidate without verified fixture + baseline grid coverage.
- `next_eligible_refresh_at` = **`2026-11-13T00:58:05.114706+00:00`**. At handoff now `2026-11-12T01:27:02Z` (independent `date -u`/Python) the gate is **NOT ELIGIBLE** (~23h31m03s / 84663s remaining). Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed.
- Preserved artifacts present: `results/FINAL_DECISION.md` (23,304 bytes), `results/20261019_135940_grid/progress.json` (1,478,918 bytes), `universe/mcap_snapshot_20261112_005805.json` (544,098 bytes). EMA signal/fill/cost assumptions unchanged. Historical research only; no orders. No duplicate wakeups scheduled.

## Your task (measurable, in order)

1. **Offline first:** read `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`, this file, and `universe/last_scan.json`. Recompute eligibility from `next_eligible_refresh_at` (`2026-11-13T00:58:05.114706+00:00`) vs independent UTC (`date -u` and/or Python); do not guess.
2. **If not eligible (expected until 2026-11-13T00:58:05.114706Z):** make **no provider calls**. Append a brief offline gate-check record (exact now/bound/remaining, state evidence, any batch/coverage notes) to `NEXT_AGENT_TASK.md` and update this file's handoff timestamp/status if you perform checks; stop. Do not schedule duplicate wakeups.
3. **If eligible:** run **at most one** 20-page snapshot pass: `PYTHONPATH=. timeout 1800 python3 scripts/fetch_mcap_snapshot.py --pages 20` (no `--apply`; script sleeps ~30s/page plus KuCoin probes). Recompute expansion floor vs included-universe fixtures, inspect below-floor band, and update `universe/last_scan.json` (snapshot path/id, scanned_at, coverage, floor, eligible_unseen_below_floor, `batch_selected`, `next_eligible_refresh_at`).
4. **Before any `--apply`:** verify fixture + baseline grid coverage in `results/20261019_135940_grid/progress.json` for **every** selected candidate. If coverage is not verified for all selected candidates, **do not run `--apply`**; record blocker per candidate and stop cleanly.
5. **Never:** rerun grids, fetch candles, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow `AGENTS.md` adaptive gate policy.
