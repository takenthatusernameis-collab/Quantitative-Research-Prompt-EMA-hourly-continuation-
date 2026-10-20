# INITIAL TASK FOR NEXT AGENT

Continue the EMA hourly-continuation research program: expand the market-cap universe by
one batch (batch 18, N 177 -> 187) if continuing the program. Batch 17 is complete. Read
`NEXT_AGENT_TASK.md` first - it has the full state, the exact commands and the guardrails.

STATE: universe N = 177 (batch 17 complete). Grid 11,682/11,682 cells, 0 credible
candidates (candidate_check 20261020_094859). Mean net PF 0.4917, best 2.2274
(BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 35 cells with net PF > 1 all rejected.

DO NEXT (batch 18, N 177 -> 187) if continuing:
1. Fresh ranking: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10`
   (dry run), then `--apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply`.
2. OHLCV: `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10>`,
   then `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest`.
   Re-query on KuCoin 400100 before treating a name as ineligible.
3. Grid, one invocation per symbol, checkpoint after each:
   `PYTHONPATH=. python3 scripts/run_grid.py --n 178` ... `--n 187` with
   `--resume results/20261019_135940_grid --note "universe expansion batch 18: N 177 -> 187 (<SYMBOL>/USDT, 66-pair EMA grid)"`,
   then `PYTHONPATH=. python3 scripts/remote_checkpoint.py --message "chore(kilo): grid batch18 <SYMBOL>/USDT (66 cells, N=187)" --paths results/20261019_135940_grid`.
4. `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid`
   then `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid`.
5. Update `NEXT_AGENT_TASK.md` and this file, checkpoint.

RULES: never promote a cell on in-sample numbers alone; keep the universe append-only
and strictly market-cap descending; do not stand down after a failed batch.

Validation: `python -m pytest tests/ -q` (46 passing at handoff).
"