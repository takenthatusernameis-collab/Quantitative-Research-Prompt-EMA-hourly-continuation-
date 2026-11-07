Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md` (latest record: 2026-11-07T08:07:28Z), `universe/last_scan.json`.

**Current state (verified 2026-11-07T08:07:28Z; source of truth `universe/last_scan.json`):**
- `next_eligible_refresh_at` = `2026-11-07T10:16:12.893046+00:00`. **NOT ELIGIBLE** at `2026-11-07T08:07:28+00:00` (direct JSON + independent UTC cross-check): `eligible=false`, `remaining_seconds=7724.89` (~2h08m45s / ~2.15h).
- `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `snapshot_id=mcap_snapshot_20261106_101612`, `snapshot_path=universe/mcap_snapshot_20261106_101612.json` (present), `scanned_at=2026-11-06T10:16:12.893046+00:00`, source=CoinGecko `/api/v3/coins/markets` (usd, market_cap_desc), coverage=20/20 pages/2000 entries, `lowest_rank_covered=2000`, `lowest_market_cap_usd=3179353`, `coverage_reaches_below_floor=true`, `universe_n=275`, `expansion_floor={PIXEL/USDT, $3,254,887}`, `eligible_unseen_below_floor_count=0`, `eligible_unseen_below_floor=[]`, `batch_selected=[]`.
- 2026-11-06T10:16 pass found 0 eligible unseen names below the floor (not a coverage shortfall; lowest covered $3,179,353 < floor $3,254,887). `data/fixtures/SUKU_USDT.csv` ABSENT; no `*SUKU*` anywhere in the tree. **`--apply` MUST NOT run** without verified fixture/grid coverage for any selected candidate.
- Baseline grid `results/20261019_135940_grid/progress.json` complete (`completed_cells=18150`, `n_symbols=275`, `n_pairs=66`, `all_symbols_processed=true`, `stopped=false`, `next_cell=null`). `results/FINAL_DECISION.md` records program-level rejection. `scripts/fetch_mcap_snapshot.py` and `scripts/refresh_gate.py` present.

**What to do:**
1. Re-verify gate eligibility at start from `universe/last_scan.json` (do not guess). NOT ELIGIBLE until `2026-11-07T10:16:12.893046+00:00`.
2. If still not eligible: make **no provider calls**. Record an offline check in `NEXT_AGENT_TASK.md` (exact now/bound/remaining, state evidence), update this handoff if needed, and stop. Rely on scheduled wakeup; do not schedule duplicates.
3. If eligible: run **at most one** 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without verified coverage.
4. Never: rerun grids, fetch candles, place orders, change EMA/cost/fill assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory.

**Constraints:** historical research only; free public data/no-cost tooling; preserve negative/blocked results; follow `AGENTS.md` gate policy. Wakeup retained: `wku_1b3cb2ba10013PChsdJTbjSl1z` due `2026-11-07T10:21:00Z` (~5 min after gate opens). **Do not re-schedule a duplicate.**
/home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-/INITIAL_TASK_FOR_NEXT_AGENT.md