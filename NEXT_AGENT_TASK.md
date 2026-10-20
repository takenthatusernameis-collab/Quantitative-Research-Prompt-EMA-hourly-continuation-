# NEXT AGENT TASK

## Status update (2026-10-20): batches 8-10 COMPLETE. Universe N=107, grid 7,062/7,062
## cells, 0 credible candidates. Next: batch 11 (N 107 -> 117).

## Objective
**Batches 8, 9 and 10 grid COMPLETE.** All 7,062 cells (107 symbols x 66 EMA pairs)
are finished; 7,060 rejected and the 2 cells that reached net PF > 1 in the scan
were killed by out-of-sample + cost stress (`results/20261020_000649_candidate_check/`).
Per PROMPT.md §2.1 the program must expand again: **N 107 -> 117** (batch 11, next 10
lower-market-cap names), fetch a fresh ranking snapshot, download OHLCV for the 10 new
names, run the full 66-pair grid (resume `results/20261019_135940_grid`), checkpoint per
symbol, re-aggregate, re-run the candidate check, and report the cumulative rejection rate.

**Do not stand down.** A prior rejection does not stop the program (PROMPT.md §2.1.4).

## State at handoff (2026-10-20)
- Universe: **N = 107** (`universe/mcap_rank.json`), snapshot `mcap_snapshot_20261019_231438`
  (CoinGecko `/api/v3/coins/markets`, fetched 2026-10-19T23:14:38Z). Batch 10 added
  MANA, XCN, ZK, NEO, CHZ, APE, IMX, AIOZ, 1INCH, XEC (all with clean KuCoin hourly
  fixtures: 20 511-22 099 bars, no gaps, no duplicates).
- Grid: **7,062 / 7,062 cells complete** in `results/20261019_135940_grid/` (107 symbols x
  66 pairs). 0 blocked. 7,060 rejected; 2 exploratory in the scan (JASMY/USDT P20_200 and
  P21_200) and both **rejected** on robustness -> **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF 0.4762, median 0.4990, **best net PF 1.0341** (JASMY/USDT P21_200).
- Cumulative rejection rate: **7,060 / 7,062 cells (99.97 %)**, 0 credible candidates.
  Cells with net PF > 1: 2 / 7,062 = 0.03 % against a ~50 % no-edge null.
- Batch 10 alone: 660 / 660 rejected, pooled mean net PF 0.5017, best 0.9891
  (IMX/USDT P34_200, max net Sharpe -0.0015).
- Batch means are flat across batches 7-10 (0.4682 / 0.5085 / 0.5210 / 0.5017):
  lower-market-cap names do not improve the registered rule.
- Per-pair pooled leaders (mean net PF over 107 symbols): P8_200 0.6726, P20_200 0.6669,
  P12_200 0.6609, P21_200 0.6584. Worst: P20_21 0.1257, P50_55 0.1859, P8_12 0.1876.
- Robustness artifact: `results/20261020_000649_candidate_check/` (script
  `scripts/candidate_check.py`, added this session). JASMY P20_200: base PF 1.0097 ->
  OOS PF 0.9068 (174 trades) -> 2x-cost PF 0.7465 -> rejected. JASMY P21_200: base PF
  1.0341 -> OOS PF 0.9167 (173 trades) -> 2x-cost PF 0.7576 -> rejected.
- Tests: **46 passed** (`python -m pytest tests/ -q`; 37 pre-existing + 9 added for
  `scripts/candidate_check.py`).
- Note: `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md` are earlier
  artifacts covering the *narrower* single-pair OOS test (5 symbols, rr=1.5, ATR
  filter). They are not invalidated by the grid program, which is a broader scan
  under PROMPT.md §2.1 and has now covered 107 symbols x 66 pairs.

## Environment note (cost this session 5 minutes)
The runner image had **no pandas/numpy/pytest** for `python3`. Install once before any
script runs:
`python3 -m pip install --break-system-packages pandas numpy pytest`
(`requests` was already present). Then use `PYTHONPATH=. python3 scripts/...`.

## Next batch (batch 11, N 107 -> 117) - concrete steps
1. `python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10` (dry run) to see
   the next 10 names below the XEC floor, then
   `python scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply`
   to write `universe/mcap_rank.json` from the reviewed snapshot.
   Expected candidates (from the 23:14 snapshot, to be re-checked on a fresh fetch):
   SNX, SUPER, DBR, RSR, EGLD, GLM, ZEN, ATH, ORCA, GALA.
   (Note: SUPER = SuperVerse, ATH = Aethir, ZEN = Horizen, EGLD = MultiversX,
   XCN from batch 10 = Onyxcoin, NFT from batch 8 = AINFT, AXS = Axie Infinity.)
2. `python scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10 new names>`
   (takes ~30 min; 10 symbols x ~220 paginated KuCoin requests). Then
   `python scripts/fetch_kucoin.py --reconcile-manifest` so the provenance manifest
   covers every fixture on disk.
3. For each new symbol in market-cap descending order, one invocation each:
   `PYTHONPATH=. python scripts/run_grid.py --n <N> --resume results/20261019_135940_grid --note "universe expansion batch 11: N 107 -> 117 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   where `--n` is the 1-based position of that symbol in the 117-symbol ranking
   (--n 108 for the first new symbol up to --n 117 for the last; do not use a single
   `--n 117` pass, so each symbol can be checkpointed on its own).
   then `PYTHONPATH=. python scripts/remote_checkpoint.py --message "chore(kilo): grid batch11 <SYMBOL>/USDT (66 cells, N=117)" --paths results/20261019_135940_grid`.
   Each symbol takes ~2 min; the per-symbol checkpoint keeps every push delta
   inside the controller's 30 s budget.
4. `PYTHONPATH=. python scripts/aggregate_grid.py --run results/20261019_135940_grid`.
5. `PYTHONPATH=. python scripts/candidate_check.py --run results/20261019_135940_grid`
   (auto-discovers every cell with net PF > 1 and runs OOS + 2x cost stress on it).
6. Append the batch-11 section to `universe/mcap_expansion_log.md` (and add its row to
   the "Grid coverage per batch" table).
7. Update this handoff and `INITIAL_TASK_FOR_NEXT_AGENT.md`, then checkpoint.

## Guardrails
- Never promote a grid cell on in-sample numbers alone (PROMPT.md §3.3): a cell needs
  OOS + cost stress before it can be called a candidate. Two cells have now cleared
  net PF > 1 in-sample and both failed those gates.
- Keep the universe append-only and strictly market-cap descending; never reorder or
  drop names already processed (PROMPT.md §2.1.2).
- Do not stand down because a batch failed; expand and continue (§2.1.4).

## Validation Command
`python -m pytest tests/ -q`
