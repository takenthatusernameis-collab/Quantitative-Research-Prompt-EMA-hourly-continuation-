# INITIAL TASK FOR NEXT AGENT

Continue the EMA hourly-continuation research program: expand the market-cap universe by
one batch (batch 14, N 137 -> 147), run the full 66-pair EMA grid on the new names, and
re-run the robustness check. Read `NEXT_AGENT_TASK.md` first - it has the full state, the
exact commands and the guardrails.

STATE: universe N = 137 (`universe/mcap_rank.json`, snapshot `mcap_snapshot_20261020_021004`).
Grid 9,042 / 9,042 cells complete in `results/20261019_135940_grid/` (137 symbols x 66
pairs), 0 blocked, 9,039 rejected, 3 exploratory in the scan (JASMY P20_200, JASMY P21_200,
SUPER P8_200) - all 3 rejected by OOS + cost stress, so **0 credible candidates**. Pooled
mean net PF 0.4833, median 0.5056, best 1.0377 (SUPER/USDT P8_200, rejected OOS),
7,498,797 trades. Cells with net PF > 1: 3 / 9,042 = 0.03 % against a ~50 % no-edge null.
Batch 13 alone: 660 cells, 660 rejected, mean net PF 0.4961, best 0.8305.

DO NEXT (batch 14, N 137 -> 147):
1. Fresh ranking + expansion: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 4
   --batch-size 10` (dry run), then `--apply-from universe/mcap_snapshot_<TS>.json
   --batch-size 10 --apply`. Expected next 10: ZETA, AXL, ALT, BABYDOGE, TFUEL, IO, DGB,
   SUSHI, EDU, RLC (re-check on the fresh fetch; keep the order strictly market-cap
   descending).
2. OHLCV: `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10>`,
   then `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest`.
   If a symbol returns KuCoin `400100`, RE-QUERY it before treating it as ineligible -
   that error was transient for all six batch-12 names.
3. Grid, one invocation per symbol, checkpoint after each:
   `PYTHONPATH=. python3 scripts/run_grid.py --n 138` ... `--n 147` with
   `--resume results/20261019_135940_grid --note "universe expansion batch 14: N 137 -> 147 (<SYMBOL>/USDT, 66-pair EMA grid)"`,
   then `PYTHONPATH=. python3 scripts/remote_checkpoint.py --message "chore(kilo): grid batch14 <SYMBOL>/USDT (66 cells, N=147)" --paths results/20261019_135940_grid`.
4. `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid`
   then `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid`.
5. Append the batch-14 section to `universe/mcap_expansion_log.md` (+ row in the
   "Grid coverage per batch" table), update `NEXT_AGENT_TASK.md` and this file, checkpoint.

RULES: never promote a cell on in-sample numbers alone (PROMPT.md §3.3 - OOS + 2x cost
stress are required); keep the universe append-only and strictly market-cap descending; do
not stand down after a failed batch (PROMPT.md §2.1.4).

Environment: `PYTHONPATH=. python3` (pandas/numpy/pytest/requests are installed; if not:
`python3 -m pip install --break-system-packages pandas numpy pytest`).

Validation: `python -m pytest tests/ -q` (46 passing at handoff).
