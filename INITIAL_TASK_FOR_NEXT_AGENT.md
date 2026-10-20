# INITIAL TASK FOR NEXT AGENT

Continue the EMA hourly-continuation research program: expand the market-cap universe by
one batch (batch 17, N 167 -> 177) if continuing the program. Batch 16 is complete., run the full 66-pair EMA grid on the new names, and
re-run the robustness check. Read `NEXT_AGENT_TASK.md` first - it has the full state, the
exact commands and the guardrails.

STATE: universe N = 167 (batch 16 complete). Last batch 16 added WIN, TRB, CELO, FLOW, ID, CTC, DEEP, BRETT, CFG, XNO; grid 11,022/11,022 cells, 0 credible candidates (candidate_check 20261020_080932). (`universe/mcap_rank.json`, snapshot `mcap_snapshot_20261020_065809`).
Grid 11,022 / 11,022 cells complete in `results/20261019_135940_grid/` (167 symbols x 66
pairs), 0 blocked, 10,997 rejected, 25 exploratory in the scan (all rejected by OOS +
cost stress), **0 credible candidates**. Pooled mean net PF 0.4922, median 0.5124,
best 2.2274 (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 9,035,501 trades.
Cells with net PF > 1: 35 / 11,022 = 0.3 % against a ~50 % no-edge null; all 35 rejected
(32 BABYDOGE cells have 0 OOS trades; JASMY P20_200/P21_200 and SUPER P8_200 fail cost
stress). Batch 16 alone: 660 cells, 660 rejected, 0 exploratory, 0 cells with net PF > 1.

DO NEXT (batch 17, N 167 -> 177) if continuing:
1. Fresh ranking + expansion: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 4
   --batch-size 10` (dry run), then `--apply-from universe/mcap_snapshot_<TS>.json
   --batch-size 10 --apply`. Expected next 10: names below XNO's $45.5M floor (re-check
   on the fresh fetch; keep the order strictly market-cap descending).
2. OHLCV: `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10>`,
   then `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest`.
   If a symbol returns KuCoin `400100`, RE-QUERY it before treating it as ineligible -
   that error was transient for all six batch-12 names.
3. Grid, one invocation per symbol, checkpoint after each:
   `PYTHONPATH=. python3 scripts/run_grid.py --n 168` ... `--n 177` with
   `--resume results/20261019_135940_grid --note "universe expansion batch 17: N 167 -> 177 (<SYMBOL>/USDT, 66-pair EMA grid)"`,
   then `PYTHONPATH=. python3 scripts/remote_checkpoint.py --message "chore(kilo): grid batch17 <SYMBOL>/USDT (66 cells, N=177)" --paths results/20261019_135940_grid`.
4. `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid`
   then `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid`.
5. Append the batch-16 section to `universe/mcap_expansion_log.md` (+ row in the
   "Grid coverage per batch" table), update `NEXT_AGENT_TASK.md` and this file, checkpoint.

RULES: never promote a cell on in-sample numbers alone (PROMPT.md §3.3 - OOS + 2x cost
stress are required); keep the universe append-only and strictly market-cap descending;
do not stand down after a failed batch (PROMPT.md §2.1.4).

Environment: `PYTHONPATH=. python3` (pandas/numpy/pytest/requests are installed; if not:
`python3 -m pip install --break-system-packages pandas numpy pytest`).

Validation: `python -m pytest tests/ -q` (46 passing at handoff).
