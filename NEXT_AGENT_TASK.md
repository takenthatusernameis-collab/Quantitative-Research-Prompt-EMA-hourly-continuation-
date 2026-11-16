# NEXT_AGENT_TASK.md — EMA hourly continuation universe-refresh gate

**Updated:** 2026-11-16T00:02:29Z (this agent: offline only, no provider calls).

Read `README.md`, `AGENTS.md`, `PROMPT.md` (§2.1.2, §2.1.5, §6), this file, `INITIAL_TASK_FOR_NEXT_AGENT.md`, `universe/last_scan.json` and `universe/mcap_rank.json` before acting.

## 1. Status

- **Gate: NOT ELIGIBLE.** now=`2026-11-16T00:02:29.203466Z` (independent `date -u` = `2026-11-16T00:02:29Z`; Python `datetime.now(timezone.utc)` = `2026-11-16T00:02:29.203466+00:00`), bound=`2026-11-16T07:28:12.929462+00:00` (`universe/last_scan.json` `next_eligible_refresh_at`), remaining ≈ **7h25m44s (26,743s)**. Reason (PROMPT.md §2.1.5): the 24 h refresh bound has not elapsed.
- Gate opens **2026-11-16T07:28:12.929462+00:00**. Status derived offline via `scripts.refresh_gate.gate_status(state)` (PYTHONPATH=.) → `eligible=false`.
- Scan state: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261115_072812`, scanned_at=`2026-11-15T07:28:12.929462+00:00`, source=CoinGecko `/api/v3/coins/markets` (usd, market_cap_desc), 25/25 pages, 2500 entries, `all_requested_pages_returned=true`, `coverage_reaches_below_floor=true`, lowest rank 2500, lowest mcap **$1,519,127**, `universe_n=276`, `batch_selected=["CERE/USDT"]`, `eligible_unseen_below_floor_count=0`.
- Expansion floor: **CERE/USDT $1,521,812** (rank 2495).
- CERE expansion is complete and audited: `grid_expansion` 2026-11-15T14:37:24.394504Z added CERE/USDT (66 cells, new_n=276, previous_n=275); `grid_verification` 2026-11-15T14:37:28.352788Z confirms 276 symbols / 18,216/18,216 cells / `cells_blocked=0` / `incomplete_symbols=[]` / `symbols_without_fixture=[]`. `universe/mcap_rank.json` updated_at=`2026-11-15T14:34:58.596658Z`, n_symbols=276, CERE/USDT last. No further CERE action is required.

## 2. Independent offline verification (2026-11-15T23:46:09Z, stdlib only, no network)

- **Floor + band re-derived** from the frozen snapshot plus `mcap_rank.json`: 276/276 universe symbols matched in the 2500-entry snapshot; lowest included market cap = **CERE/USDT $1,521,812**; **0 eligible unseen** entries strictly below the floor.
- **5 entries strictly below the floor** (all excluded): rank 2496 VAPI $1,521,123 `no_tradable_kucoin_spot_usdt_pair`; 2497 GM $1,519,405 `no_tradable_kucoin_spot_usdt_pair`; 2498 OFC $1,519,208 `insufficient_hourly_history_for_grid`; 2499 FUSD $1,519,196 `no_tradable_kucoin_spot_usdt_pair`; 2500 WFRAGSOL $1,519,127 `no_tradable_kucoin_spot_usdt_pair`. Structural coverage is sufficient either way.
- Terminology correction retained from earlier passes: the "55 entries, ranks 2446-2500" figure was the tail window *including* the floor symbol CERE (rank 2495) = 50 `no_tradable_kucoin_spot_usdt_pair` + 4 `insufficient_hourly_history_for_grid` + 1 eligible (CERE, already processed). Only 54 entries sit strictly below $1,610,416 (ranks 2447-2500).
- **Grid:** `results/20261019_135940_grid/progress.json` — `n_symbols=276`, `n_pairs=66`, `completed_cells=18216` = 276×66, `stopped=false`, `all_symbols_processed=true`; 0 universe symbols missing a fixture under `data/fixtures/`.
- **Artifacts:** `results/FINAL_DECISION.md` 23,304 B; `results/20261019_135940_grid/progress.json` 1,484,320 B; `universe/mcap_snapshot_20261115_072812.json` 683,184 B; `universe/last_scan.json`; `universe/mcap_rank.json` 5,003 B (276 symbols); `data/fixtures/CERE_USDT.csv` 1,601,043 B.
- **Environment:** `python3` 3.12.3 lacks `pandas`, `numpy`, `pytest` (`requests` 2.31.0 present). `scripts/refresh_gate.py` (stdlib) and `scripts/fetch_mcap_snapshot.py` (stdlib + requests) run here; `scripts/refresh_universe.py`, `scripts/refresh_audit.py`, `scripts/aggregate_grid.py` and the grid runner import `pandas` and cannot run until dependencies are installed.
- `cron_list` empty (no wakeups scheduled). `git status --short` clean before this handoff edit. Historical research only; no orders.

## 3. What this session did

- Recomputed the gate offline (`scripts.refresh_gate.gate_status`, PYTHONPATH=.); gate closed (eligible=false, remaining ~7h30m), so **no provider calls**, no snapshot/candle fetch, no `--apply`, no grid rerun.
- Appended one gate-check line to both handoff logs. No research artifacts or assumptions were changed.

## 4. Your task (one measurable task)

1. **Offline first:** read the files listed above. Recompute eligibility from `next_eligible_refresh_at` vs independent UTC (`date -u` and `datetime.now(timezone.utc)`); never guess.
2. **If NOT eligible (expected until 2026-11-16T07:28:12Z):** make **no provider calls**. Append exactly one concise offline gate-check line (exact now/bound/remaining, state evidence) to the gate-check log below and to `INITIAL_TASK_FOR_NEXT_AGENT.md`; stop. Do not schedule wakeups (`cron_list` must stay empty).
3. **If eligible (after 2026-11-16T07:28:12Z):** run **at most one** snapshot pass with enough pages to reach below the current floor: `PYTHONPATH=. timeout 1800 python3 scripts/fetch_mcap_snapshot.py --pages 25` (no `--apply`; ~30 s/page sleeps plus KuCoin probes; 20 pages previously stopped above the floor, so 20 is insufficient). Recompute the floor vs included-universe fixtures (`included_market_caps` / `expansion_floor` / `select_expansion_candidates`), inspect the below-floor band (strictly below the floor, excluding the floor symbol), and update `universe/last_scan.json`. If no eligible candidate remains, record `AWAITING_NEW_ELIGIBLE_CANDIDATES`; if the pass stops above the floor, record `INCOMPLETE_SCAN` rather than claiming the band is empty.
4. **Before any `--apply`:** verify fixture + baseline grid coverage in `results/20261019_135940_grid/progress.json` for **every** selected candidate. If any candidate lacks either, **do not apply**; record the blocker per candidate and stop cleanly.
5. **Never:** rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow the AGENTS.md adaptive gate policy.

**One measurable next task:** perform exactly one offline gate evaluation (gate is closed until 2026-11-16T07:28:12Z), update both handoff files, and stop.

## 5. Gate-check log (compact)

All checks are offline, stdlib-only, no provider calls, no `--apply`, no grid reruns. `bound` was `2026-11-16T07:28:12.929462+00:00` in every row; state was `AWAITING_NEW_ELIGIBLE_CANDIDATES` with `eligible_unseen_below_floor_count=0` in every row.

| UTC now | Remaining | Outcome |
| --- | --- | --- |
| 2026-11-15T14:49:24Z | 16h38m48.5s | NOT ELIGIBLE; same state |
| 2026-11-15T20:18:50Z | 11h09m22.6s | NOT ELIGIBLE; 5 entries below floor |
| 2026-11-15T20:22:26Z | 11h05m46.9s | NOT ELIGIBLE; 5 entries below floor |
| 2026-11-15T20:26:17Z | 11h01m55.8s | NOT ELIGIBLE; 5 entries below floor |
| 2026-11-15T20:30:00Z | 10h58m12.0s | NOT ELIGIBLE; 5 entries below floor |
| 2026-11-15T20:34:21Z | 10h53m51.7s | NOT ELIGIBLE; 5 entries below floor |
| 2026-11-15T20:43:18Z | 10h44m54.6s | NOT ELIGIBLE; floor/band and 18,216-cell grid independently re-verified |
| 2026-11-15T20:44:19Z | 10h43m53.2s | NOT ELIGIBLE; offline gate recomputed (eligible=false), no provider calls |
| 2026-11-15T23:44:36Z | 7h43m36.7s | NOT ELIGIBLE; offline gate recomputed via scripts.refresh_gate.gate_status (eligible=false, state=AWAITING_NEW_ELIGIBLE_CANDIDATES, eligible_unseen_below_floor_count=0), no provider calls |
| 2026-11-15T23:46:09Z | 7h42m03.4s | NOT ELIGIBLE; offline gate recomputed via scripts.refresh_gate.gate_status (eligible=false, state=AWAITING_NEW_ELIGIBLE_CANDIDATES, eligible_unseen_below_floor_count=0), no provider calls |
| 2026-11-15T23:50:01Z | 7h38m04s | NOT ELIGIBLE; offline gate recomputed via scripts.refresh_gate.gate_status (eligible=false, state=AWAITING_NEW_ELIGIBLE_CANDIDATES, eligible_unseen_below_floor_count=0), no provider calls |
| 2026-11-15T23:55:07Z | 7h33m05s | NOT ELIGIBLE; offline gate recomputed via scripts.refresh_gate.gate_status (eligible=false, state=AWAITING_NEW_ELIGIBLE_CANDIDATES, eligible_unseen_below_floor_count=0), no provider calls |
| 2026-11-15T23:58:24Z | 7h29m48s | NOT ELIGIBLE; offline gate recomputed via scripts.refresh_gate.gate_status (eligible=false, state=AWAITING_NEW_ELIGIBLE_CANDIDATES, eligible_unseen_below_floor_count=0), no provider calls |
| 2026-11-16T00:02:29Z | 7h25m44s (26,743s) | NOT ELIGIBLE; offline gate recomputed via scripts.refresh_gate.gate_status (eligible=false, state=AWAITING_NEW_ELIGIBLE_CANDIDATES, eligible_unseen_below_floor_count=0), no provider calls |
