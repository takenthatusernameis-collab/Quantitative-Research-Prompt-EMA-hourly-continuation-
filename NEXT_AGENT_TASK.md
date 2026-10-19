# NEXT AGENT TASK

## Objective
**Active / in progress.** The EMA hourly-continuation program continues under PROMPT.md §2.1 and §3.4:
every `(symbol, P_fast, P_slow)` cell tested so far is net-PF < 1 (**rejected**), so the program must
**expand the universe to the next lower market-cap batch** and run the **full 66-pair EMA grid** on it.
Do **not** stand down on the grounds that the strategy failed: a rejection never halts this program.

Authoritative rules: `PROMPT.md` (updated 2026-10-19). The earlier "CONCLUDED / REJECTED" handoff
(kept for history in `NEXT_AGENT_TASK.md.updated`) described only the EMA 50/100 pair on the top-5
names and was superseded by the user-authorized grid + expanding-universe program.

## State at handoff (2026-10-19)
- **Universe:** N = 27, market-cap descending, in `universe/mcap_rank.json`
  (snapshot `mcap_snapshot_20261019_144235`, CoinGecko `/api/v3/coins/markets`,
  `order=market_cap_desc`, fetched 2026-10-19T14:42:35Z). Full expansion history, ranks, market caps
  and rank drift: `universe/mcap_expansion_log.md`.
- **Grid:** **1122 / 1122 cells complete** (17 symbols x 66 EMA pairs) in `results/20261019_135940_grid/`
  (aggregates `pooled.md`, `per_symbol.json`, `per_pair.json`, `summary.json` sit in that directory).
- **Decision: every cell rejected.** 0 cells with net PF > 1 out of 1122 tested; cumulative rejection
  rate **1122 / 1122 = 100.0 %**; 0 credible candidates, 0 exploratory signals, 0 blocked cells.
- **Pooled (net of costs):** 927 431 trades, mean net PF 0.4067, median 0.4222, best net PF **0.9219**
  (NEAR/USDT P26_200), mean net Sharpe -8.4612, best net Sharpe -0.4228 (NEAR/USDT P26_200).
  Every one of the 66 EMA pairs has mean net PF < 1 across the 17 symbols.
- **Data:** hourly OHLCV for all 27 symbols, provenance in `data/fixtures/fetch_manifest.json`
  (KuCoin public `/api/v1/market/candles`, 1h, UTC; 22 000 bars per name, BTC 25 000).
- **Tests:** `python -m pytest tests/ -q` -> **37 passed**.

## Next action
1. **Run the full 66-pair grid on the 10 newly added lower-market-cap symbols.** The universe has
   already been expanded to N = 27 and the OHLCV for the new names is already downloaded, so no
   ranking or fetch work is needed:
   - Batch 3 (all strictly below AVAX, the previous floor of $4 258 366 460), market-cap descending:
     **SUI** ($4.064 B, snapshot rank 29), **GRAM** ($3.782 B, 31), **HBAR** ($3.629 B, 32),
     **TAO** ($3.032 B, 35), **SHIB** ($2.933 B, 36), **CRO** ($2.911 B, 37), **QNT** ($2.829 B, 40),
     **ENA** ($2.476 B, 41), **AAVE** ($2.272 B, 46), **ONDO** ($2.103 B, 48).
   - Command (resumes from `progress.json`; the 17 finished symbols are skipped automatically):
     ```
     PYTHONPATH=. python scripts/run_grid.py --resume results/20261019_135940_grid --n 27 \
         --taker-fee-bps 10 --slippage-bps 2 --rr 1.0 \
         --note "universe expansion batch 3 (CoinGecko snapshot mcap_snapshot_20261019_144235): N 17 -> 27"
     ```
   - **Checkpoint after every symbol** (see "Remote persistence" below), then re-aggregate:
     `python scripts/aggregate_grid.py --run results/20261019_135940_grid`.
   - If those 10 are rejected as well (expected from the current 100 % rejection rate), **expand again**
     (§2.1): fetch a fresh ranking
     `python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10 --apply`, download the OHLCV
     `python scripts/fetch_kucoin.py --symbols <BASE>/USDT ... --target-bars 22000`, and repeat the
     full grid. A rejection is never a stop condition.
2. **Report** the new cumulative rejection rate, the per-symbol and per-pair tables, and the
   N -> N+10 expansion in the handoff. Do not promote a single lucky cell: 1122 cells have been
   tested so far, so a cell with net PF slightly above 1 would be a multiple-testing artefact, not an
   edge (PROMPT.md §3.3).

## Remote persistence (critical - read before starting any long job)
The supervising workflow checkpoints with a **30 second** remote write budget
(`.github/workflows/main.yml` -> `persist_checkpoint()`:
`timeout --kill-after=5s 30s git push origin HEAD:$DEFAULT_BRANCH`). `git push` has to build a delta
pack *before* it uploads anything. Measured on this 4-core runner, the ~450 MB of new grid artifacts
produced by the previous session needed **~34 s just to build the pack and ~44 s in total**, so every
attempt was killed by `timeout`, the checkpoint was reported as unpersisted, and that worker session
was terminated (that is what ended session 58). The same payload now pushes in ~10 s because of the
two mitigations below - use both.

1. **Bulk artifacts are gzip-compressed.** A cell stores `trades.csv.gz` and `equity.csv.gz`
   (~227 KB per cell instead of ~2.0 MB, i.e. ~4.7x smaller; a full 66-cell symbol is ~15 MB instead
   of ~130 MB). Read them with `gzip -dc <file>` or
   `pandas.read_csv(path, compression="gzip")`; `scripts/run_grid.py` exposes `read_artifact_csv()`
   for both the new `.gz` and the legacy plain `.csv` layout.
   The five top-ranked symbols in `results/20261019_135940_grid/` were written before this change and
   still carry plain `trades.csv` / `equity.csv` - that is expected, not a bug.
2. **`scripts/remote_checkpoint.py`** commits a small delta, pushes it and verifies the remote SHA.
   Run it **after every symbol** so the controller's own end-of-session push has almost nothing left
   to send:
   ```
   python scripts/remote_checkpoint.py --message "chore(kilo): grid batch3 SUI" \
       --paths results/20261019_135940_grid/results/SUI_USDT \
              results/20261019_135940_grid/progress.json \
              results/20261019_135940_grid/run_config.json
   ```
   Never batch a whole multi-symbol grid into one checkpoint - that is exactly what timed out.
   `--paths` also keeps a checkpoint from picking up a data file that is still being downloaded.

## Constraints
- Do not invent symbols; expand by market capitalisation descending only.
- Do not delete or rewrite prior artifacts (the rejected 50/100 baseline and the plain-CSV cells stay).
- Do not claim an edge without OOS net-of-costs evidence plus robustness; report the full grid
  honestly.
- Do not modify `.github/workflows/main.yml`; the controller reverts workflow files at every checkpoint.
- A rejection on one pair or one symbol never halts the program; document it and continue.

## Validation
`python -m pytest tests/ -q`
