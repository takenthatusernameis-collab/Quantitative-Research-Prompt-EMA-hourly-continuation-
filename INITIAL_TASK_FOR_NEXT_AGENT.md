# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Handoff written:** 2026-11-15T23:50:01Z (offline only, no provider calls). Read `README.md`, `AGENTS.md`, `PROMPT.md` (§2.1.2, §2.1.5), `NEXT_AGENT_TASK.md`, `universe/last_scan.json` and `universe/mcap_rank.json` first.

## 1. Status at handoff

- **Gate: NOT ELIGIBLE.** now=`2026-11-15T23:50:01.524276+00:00` (independent `date -u` = `2026-11-15T23:50:01Z`; Python `datetime.now(timezone.utc)`), bound=`2026-11-16T07:28:12.929462+00:00` (`universe/last_scan.json` `next_eligible_refresh_at`), remaining ≈ **7h38m04s (27,484s)**. Reason (PROMPT.md §2.1.5): the 24 h refresh bound has not elapsed. Gate opens **2026-11-16T07:28:12.929462+00:00**. Derived offline with `scripts.refresh_gate.gate_status(state)` (PYTHONPATH=.) → `eligible=false`.
- Scan state: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261115_072812`, scanned_at=`2026-11-15T07:28:12.929462+00:00`, CoinGecko `/api/v3/coins/markets` (usd, market_cap_desc), 25/25 pages, 2500 entries, `coverage_reaches_below_floor=true`, lowest mcap **$1,519,127**, universe_n=276, expansion floor **CERE/USDT $1,521,812** (rank 2495), `eligible_unseen_below_floor_count=0`, `batch_selected=["CERE/USDT"]`.
- Below-floor band: **5 entries strictly below the floor**, all excluded — VAPI $1,521,123 and GM $1,519,405 and FUSD $1,519,196 and WFRAGSOL $1,519,127 (`no_tradable_kucoin_spot_usdt_pair`), OFC $1,519,208 (`insufficient_hourly_history_for_grid`); **0 eligible unseen**.
- Grid: 276 symbols × 66 pairs = **18,216/18,216 cells complete** (`results/20261019_135940_grid/progress.json`), `cells_blocked=0`, `incomplete_symbols=[]`, `symbols_without_fixture=[]`, `all_symbols_processed=true`. CERE/USDT expansion (66 cells, previous_n=275 → new_n=276) is complete and audited; no further CERE action is needed.
- Preserved artifacts present: `results/FINAL_DECISION.md` (23,304 B), `results/20261019_135940_grid/progress.json` (1,484,320 B), `universe/mcap_snapshot_20261115_072812.json` (683,184 B), `universe/mcap_rank.json` (5,003 B, 276 symbols), `data/fixtures/CERE_USDT.csv` (1,601,043 B). `cron_list` empty. `git status --short` clean before handoff edits. No provider calls, no snapshot/candle fetch, no `--apply`, no grid reruns, no EMA signal/fill/cost changes, no orders.
- **Environment:** `python3` 3.12.3 without `pandas`, `numpy`, `pytest`; `requests` 2.31.0 present. `scripts/refresh_gate.py` (stdlib) and `scripts/fetch_mcap_snapshot.py` (stdlib + requests) run here. `scripts/refresh_universe.py` and the grid/aggregation scripts import `pandas` and cannot run until dependencies are installed.

## 2. Your task (measurable, one item)

1. **Offline first.** Recompute eligibility from `next_eligible_refresh_at` (`2026-11-16T07:28:12.929462+00:00`) against independent UTC (`date -u` and `datetime.now(timezone.utc)`); never guess. Expected **NOT ELIGIBLE** until the gate opens.
2. **If NOT eligible (expected until 2026-11-16T07:28:12Z):** make **no provider calls**. Append exactly one concise offline gate-check line (exact now/bound/remaining, state evidence) to the gate-check log in `NEXT_AGENT_TASK.md` and to section 4 below; stop. Do not schedule wakeups (`cron_list` must stay empty).
3. **If eligible (after 2026-11-16T07:28:12Z):** run **at most one** snapshot pass deep enough to reach below the current floor: `PYTHONPATH=. timeout 1800 python3 scripts/fetch_mcap_snapshot.py --pages 25` (no `--apply`; ~30 s/page sleeps plus KuCoin probes; 20 pages previously stopped above the floor). Recompute the floor via `included_market_caps` / `expansion_floor` / `select_expansion_candidates`, inspect the band strictly below the floor (excluding the floor symbol), and update `universe/last_scan.json`. If nothing eligible remains, record `AWAITING_NEW_ELIGIBLE_CANDIDATES`; if the pass stops above the floor, record `INCOMPLETE_SCAN` rather than claiming an empty band.
4. **Before any `--apply`:** verify fixture + baseline grid coverage in `results/20261019_135940_grid/progress.json` for **every** selected candidate. If any candidate lacks either, **do not apply**; record the blocker per candidate and stop cleanly.
5. **Never:** rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow the AGENTS.md adaptive gate policy.

## 3. Evidence already verified offline (do not redo)

- 276/276 universe symbols matched the frozen snapshot; floor reproduced as CERE/USDT $1,521,812; 0 eligible unseen entries strictly below it.
- 18,216 = 276 × 66 grid cells complete; 0 universe symbols missing a fixture.
- Artifact sizes and `last_scan.json` state as listed in section 1.

## 4. Gate-check log (append one line per offline check)

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
