# INITIAL TASK FOR NEXT AGENT

Continue the EMA hourly-continuation research program: expand the market-cap universe by
one batch (batch 16, N 157 -> 167) if continuing the program. Batch 15 is complete., run the full 66-pair EMA grid on the new names, and
re-run the robustness check. Read `NEXT_AGENT_TASK.md` first - it has the full state, the
exact commands and the guardrails.

STATE: universe N = 157 (batch 15 complete). Last batch 15 added RLC, ROSE, TURBO, XPR, ENJ, T, ONT, ASTR, PHA, MEME; grid 10,362/10,362 cells, 0 credible candidates (candidate_check 20261020_062438). (`universe/mcap_rank.json`, snapshot `mcap_snapshot_20261020_030608`).
Grid 9,702 / 9,702 cells complete in `results/20261019_135940_grid/` (147 symbols x 66
pairs), 0 blocked, 9,677 rejected, 25 exploratory in the scan (all rejected by OOS +
cost stress), **0 credible candidates**. Pooled mean net PF 0.4894, median 0.5098,
best 2.2274 (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 7,998,391 trades.
Cells with net PF > 1: 35 / 9,702 = 0.4 % against a ~50 % no-edge null; all 35 rejected
(32 BABYDOGE cells have 0 OOS trades; JASMY P20_200/P21_200 and SUPER P8_200 fail cost
stress). Batch 14 alone: 660 cells, 638 rejected, 22 exploratory (all BABYDOGE),
0 cells with net PF > 1 outside BABYDOGE.

DO NEXT (batch 16, N 157 -> 167) if continuing:
1. Fresh ranking + expansion: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 4
   --batch-size 10` (dry run), then `--apply-from universe/mcap_snapshot_<TS>.json
   --batch-size 10 --apply`. Expected next 10: names below DEXE's $61.4M floor (re-check
   on the fresh fetch; keep the order strictly market-cap descending).
2. OHLCV: `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10>`,
   then `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest`.
   If a symbol returns KuCoin `400100`, RE-QUERY it before treating it as ineligible -
   that error was transient for all six batch-12 names.
3. Grid, one invocation per symbol, checkpoint after each:
   `PYTHONPATH=. python3 scripts/run_grid.py --n 158` ... `--n 167` with
   `--resume results/20261019_135940_grid --note "universe expansion batch 16: N 157 -> 167 (<SYMBOL>/USDT, 66-pair EMA grid)"`,
   then `PYTHONPATH=. python3 scripts/remote_checkpoint.py --message "chore(kilo): grid batch16 <SYMBOL>/USDT (66 cells, N=167)" --paths results/20261019_135940_grid`.
4. `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid`
   then `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid`.
5. Append the batch-15 section to `universe/mcap_expansion_log.md` (+ row in the
   "Grid coverage per batch" table), update `NEXT_AGENT_TASK.md` and this file, checkpoint.

RULES: never promote a cell on in-sample numbers alone (PROMPT.md §3.3 - OOS + 2x cost
stress are required); keep the universe append-only and strictly market-cap descending;
do not stand down after a failed batch (PROMPT.md §2.1.4).

Environment: `PYTHONPATH=. python3` (pandas/numpy/pytest/requests are installed; if not:
`python3 -m pip install --break-system-packages pandas numpy pytest`).

Validation: `python -m pytest tests/ -q` (46 passing at handoff).
