# Initial task for the next agent

## What is done
The EMA hourly-continuation grid batch 3 (universe expansion N 17 -> 27) is
complete. All 27 symbols x 66 EMA pairs = 1,782 cells are finished in
`results/20261019_135940_grid/`; every cell is rejected:

- 0 cells with net PF > 1 out of 1,782 tested (cumulative rejection rate
  100.0 %); 0 credible candidates, 0 exploratory signals, 0 blocked cells.
- Pooled (net of costs): 1,483,132 trades, mean net PF 0.4389, best net PF
  0.9219 (NEAR/USDT P26_200), best net Sharpe -0.4228 (NEAR/USDT P26_200).
- Tests: `python -m pytest tests/ -q` -> 37 passed.

Universe: N = 27 in `universe/mcap_rank.json`
(snapshot `mcap_snapshot_20261019_144235`, CoinGecko, fetched
2026-10-19T14:42:35Z). Batch 3 added SUI, GRAM, HBAR, TAO, SHIB, CRO, QNT,
ENA, AAVE, ONDO (all strictly below AVAX's ~$4.258 B). Full history in
`universe/mcap_expansion_log.md`.

No edge was found. Per PROMPT.md §2.1 / §3.4, a rejection never halts the
program: once the current snapshot's eligible candidates are exhausted, the
universe must be expanded to the next lower market-cap batch.

## Your job: run batch 4 (universe N 27 -> 37)

1. **Fetch a fresh market-cap ranking** (§2.1):
   ```
   python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10 --apply
   ```
   This appends the next 10 names below ONDO (~$2.103 B, the current floor)
   that are not already in the universe, in strictly descending market cap.
   Update `universe/mcap_rank.json` and log the expansion in
   `universe/mcap_expansion_log.md` (previous N -> new N, rank range added,
   source/date of the ranking).

2. **Download OHLCV for the 10 new names**:
   ```
   python scripts/fetch_kucoin.py --symbols <BASE>/USDT ... --target-bars 22000
   ```
   Store under `data/fixtures/` and update `data/fixtures/fetch_manifest.json`.

3. **Run the full 66-pair grid** on the 10 new symbols (resumes from
   `progress.json`; the 27 finished symbols are skipped automatically):
   ```
   PYTHONPATH=. python scripts/run_grid.py --resume results/20261019_135940_grid --n 37 \
       --taker-fee-bps 10 --slippage-bps 2 --rr 1.0 \
       --note "universe expansion batch 4: N 27 -> 37"
   ```

4. **Checkpoint after every symbol** (remote `git push` budget is 30 s; never
   batch a whole grid into one checkpoint - that is what timed out before):
   ```
   python scripts/remote_checkpoint.py --message "chore(kilo): grid batch4 <SYM>" \
       --paths results/20261019_135940_grid/results/<SYM>_USDT \
              results/20261019_135940_grid/progress.json \
              results/20261019_135940_grid/run_config.json
   ```
   Bulk artifacts are gzip-compressed (`trades.csv.gz`, `equity.csv.gz`);
   read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

5. **Re-aggregate**:
   `python scripts/aggregate_grid.py --run results/20261019_135940_grid`

6. **Validate**: `python -m pytest tests/ -q`

## What to report
The new cumulative rejection rate, the per-symbol and per-pair tables, and the
N 27 -> 37 expansion. Do not promote a single lucky cell: 1,782 cells have been
tested so far, so a cell with net PF slightly above 1 would be a
multiple-testing artefact, not an edge (PROMPT.md §3.3).

If the 10 new names are rejected too (expected from the 100 % rejection rate),
expand again: fetch a fresh ranking, download OHLCV, repeat the full grid. A
rejection never halts the program - document it and continue.

Full detail and the remote-persistence rules: see `NEXT_AGENT_TASK.md`.
