# NEXT AGENT TASK

## Objective
**Batch 3 grid (universe N 17 -> 27) is COMPLETE.** All 27 symbols x 66 EMA
pairs = 1,782 cells are finished in `results/20261019_135940_grid/`; every cell
is rejected (0 cells with net PF > 1; best net PF 0.9219 at NEAR/USDT P26_200;
best net Sharpe -0.4228; pooled mean net PF 0.4389 over 1,483,132 trades).
Tests: `python -m pytest tests/ -q` -> 37 passed.

Per PROMPT.md §2.1 / §3.4, a rejection never halts the program: once the
current snapshot's eligible candidates are exhausted (all processed through the
full EMA grid), the universe must be **expanded to the next lower market-cap
batch**. The next step is batch 4: **N 27 -> 37**. Do not stand down on the
grounds that the strategy failed.

Authoritative rules: `PROMPT.md` (updated 2026-10-19).

## State at handoff (2026-10-19)
- **Universe:** N = 27, market-cap descending, in `universe/mcap_rank.json`
  (snapshot `mcap_snapshot_20261019_144235`, CoinGecko `/api/v3/coins/markets`,
  `order=market_cap_desc`, fetched 2026-10-19T14:42:35Z). Full expansion
  history, ranks, market caps and rank drift: `universe/mcap_expansion_log.md`.
- **Grid:** **1,782 / 1,782 cells complete** (27 symbols x 66 EMA pairs) in
  `results/20261019_135940_grid/` (aggregates `pooled.md`, `per_symbol.json`,
  `per_pair.json`, `summary.json` sit in that directory).
- **Decision: every cell rejected.** 0 cells with net PF > 1 out of 1,782
  tested; cumulative rejection rate **1,782 / 1,782 = 100.0 %**; 0 credible
  candidates, 0 exploratory signals, 0 blocked cells.
- **Pooled (net of costs):** 1,483,132 trades, mean net PF 0.4389, median
  0.4494, best net PF **0.9219** (NEAR/USDT P26_200), mean net Sharpe -7.9760,
  best net Sharpe -0.4228 (NEAR/USDT P26_200). Every one of the 66 EMA pairs
  has mean net PF < 1 across the 27 symbols.
- **Data:** hourly OHLCV for all 27 symbols, provenance in
  `data/fixtures/fetch_manifest.json` (KuCoin public `/api/v1/market/candles`,
  1h, UTC; 22 000 bars per name, BTC 25 000).
- **Tests:** `python -m pytest tests/ -q` -> **37 passed**.

## Next action
1. **Expand the universe to the next lower market-cap batch (N 27 -> 37).**
   - Fetch a fresh ranking (§2.1):
     `python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10 --apply`
     This appends the next 10 names below ONDO (the current floor, ~$2.103 B)
     that are not already in the universe, in strictly descending market cap.
     Update `universe/mcap_rank.json` and log the expansion in
     `universe/mcap_expansion_log.md` (previous N -> new N, rank range added,
     source/date of the ranking used).
   - Download OHLCV for the 10 new names:
     `python scripts/fetch_kucoin.py --symbols <BASE>/USDT ... --target-bars 22000`
     (store under `data/fixtures/`, update `data/fixtures/fetch_manifest.json`).
   - Run the full 66-pair grid on the 10 new symbols (resumes from
     `progress.json`; the 27 finished symbols are skipped automatically):
     ```
     PYTHONPATH=. python scripts/run_grid.py --resume results/20261019_135940_grid --n 37 \
         --taker-fee-bps 10 --slippage-bps 2 --rr 1.0 \
         --note "universe expansion batch 4: N 27 -> 37"
     ```
   - **Checkpoint after every symbol** (remote write budget is 30s; never batch a
     whole grid into one checkpoint - that is exactly what timed out before):
     ```
     python scripts/remote_checkpoint.py --message "chore(kilo): grid batch4 <SYM>" \
         --paths results/20261019_135940_grid/results/<SYM>_USDT \
                results/20261019_135940_grid/progress.json \
                results/20261019_135940_grid/run_config.json
     ```
   - Re-aggregate: `python scripts/aggregate_grid.py --run results/20261019_135940_grid`.
2. **Report** the new cumulative rejection rate, the per-symbol and per-pair
   tables, and the N 27 -> 37 expansion in the handoff. Do not promote a single
   lucky cell: 1,782 cells have been tested so far, so a cell with net PF
   slightly above 1 would be a multiple-testing artefact, not an edge
   (PROMPT.md §3.3).
3. If those 10 are rejected as well (expected from the current 100 % rejection
   rate), **expand again** (§2.1): fetch a fresh ranking, download OHLCV, and
   repeat the full grid. A rejection on one pair or one symbol never halts the
   program; document it and continue.

## Remote persistence (critical - read before starting any long job)
The supervising workflow checkpoints with a **30 second** remote write budget
(`.github/workflows/main.yml` -> `persist_checkpoint()`:
`timeout --kill-after=5s 30s git push origin HEAD:$DEFAULT_BRANCH`). `git push`
has to build a delta pack *before* it uploads anything. Measured on this
4-core runner, ~450 MB of new grid artifacts needed ~34 s just to build the
pack, so every prior attempt was killed. The same payload now pushes in ~10 s
because of the two mitigations below - use both.

1. **Bulk artifacts are gzip-compressed.** A cell stores `trades.csv.gz` and
   `equity.csv.gz` (~227 KB per cell instead of ~2.0 MB, i.e. ~4.7x smaller;
   a full 66-cell symbol is ~15 MB instead of ~130 MB). Read them with
   `gzip -dc <file>` or `pandas.read_csv(path, compression="gzip")`;
   `scripts/run_grid.py` exposes `read_artifact_csv()` for both the new `.gz`
   and the legacy plain `.csv` layout. The five top-ranked symbols were written
   before this change and still carry plain `trades.csv` / `equity.csv` - that
   is expected, not a bug.
2. **`scripts/remote_checkpoint.py`** commits a small delta, pushes it and
   verifies the remote SHA. Run it **after every symbol** so the controller's
   own end-of-session push has almost nothing left to send (see the command
   above). Never batch a whole multi-symbol grid into one checkpoint.
   `--paths` also keeps a checkpoint from picking up a data file that is still
   being downloaded.

## Constraints
- Do not invent symbols; expand by market capitalisation descending only.
- Do not delete or rewrite prior artifacts (the rejected baseline and the
  plain-CSV cells stay).
- Do not claim an edge without OOS net-of-costs evidence plus robustness;
  report the full grid honestly.
- Do not modify `.github/workflows/main.yml`; the controller reverts workflow
  files at every checkpoint.
- A rejection on one pair or one symbol never halts the program; document it
  and continue.

## Validation
`python -m pytest tests/ -q`
