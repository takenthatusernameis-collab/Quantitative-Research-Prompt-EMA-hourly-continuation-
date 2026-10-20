# NEXT AGENT TASK

## Status update (2026-10-20): batch 17 COMPLETE. Universe N=177, grid 11,682/11,682 cells, 0 credible candidates. Expansion exhausted (no eligible names below floor).

## Objective

**Program complete - no further market-cap expansion possible.** All eligible names below the XNO floor have been processed (N reached 177). The full grid covers 177 symbols x 66 EMA pairs = 11,682 cells. All cells have been evaluated; 0 credible candidates survive OOS + cost stress (candidate_check 20261020_094859). Do **not** expand further - there are no additional eligible symbols available under PROMPT.md §2.1.2.

## State at handoff (2026-10-20)

- Universe: **N = 177** (`universe/mcap_rank.json`), snapshot `mcap_snapshot_20261020_065809` extended by batches 1-17. Batch 17 added BOME, ANKR, ZIL, MASK, LSK, POPCAT, AURORA, POLYX, REQ, YXYO? Wait - looking up batch 17 symbols from git history: commits show "grid batch17 BOME/USDT", "ANKR/USDT", "ZIL/USDT" etc. Final batch 17 added: XYO, POLYX, AURORA, POPCAT, REQ, LSK, MASK, ZIL, ANKR, BOME (from expansion log end).
- Grid: **11,682 / 11,682 cells complete** in `results/20261019_135940_grid/` (177 symbols x 66 pairs). 0 blocked. 11,657 rejected; 25 exploratory in the scan, all **rejected** on robustness -> **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF 0.4917, median ~0.512, **best net PF 2.2274** (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 9,595,942+ trades.
- Cumulative rejection rate: **11,657 / 11,682 cells (~99.79 %)**, 0 credible candidates.
- Cells with net PF > 1: 35 / 11,682 = ~0.3 % against a ~50 % no-edge null. All 35 failed OOS + cost stress.
- Robustness artifact: `results/20261020_094859_candidate_check/` (script `scripts/candidate_check.py`). All net-PF > 1 cells rejected.
- Data layer: 177 fixtures in `data/fixtures/` (+ sample_hourly.csv), provenance in `data/fixtures/fetch_manifest.json` (KuCoin public `/api/v1/market/candles`, 1h, UTC).
- Tests: **46 passed** (`python -m pytest tests/ -q`).

## Environment note

`python3` has pandas/numpy/pytest/requests available. Always run scripts as `PYTHONPATH=. python3 scripts/...`.

## No further expansion possible

Checked latest CoinGecko snapshots (pages 4-5). After including down to XNO (batch 16) and completing batch 17 (XYO, POLYX, AURORA, POPCAT, REQ, LSK, MASK, ZIL, ANKR, BOME), the next eligible names below the floor all fail filters (no KuCoin USDT pair / insufficient history / excluded) or don't exist. **Do not stand down prematurely** - the program is complete as specified.

## Guardrails

- Never promote a grid cell on in-sample numbers alone (PROMPT.md §3.3): a cell needs OOS + cost stress before it can be called a candidate. Every cell that has ever reached net PF > 1 in this program failed both out-of-sample and cost stress.
- Universe is append-only and strictly market-cap descending (complete).
- Do not fabricate expansion batches.

## Validation Command

`python -m pytest tests/ -q`
