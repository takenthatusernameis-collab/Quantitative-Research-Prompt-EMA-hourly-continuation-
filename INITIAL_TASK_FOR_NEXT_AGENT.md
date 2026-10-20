# INITIAL TASK FOR NEXT AGENT

Continue the EMA hourly-continuation research program: expand the market-cap universe by
one batch (batch 13, N 127 -> 137), run the full 66-pair EMA grid on the new names, and
re-run the robustness check. Read `NEXT_AGENT_TASK.md` first - it has the full state, the
exact commands and the guardrails.

STATE: universe N = 127 (`universe/mcap_rank.json`, snapshot `mcap_snapshot_20261020_011116`).
Grid 8,382 / 8,382 cells complete in `results/20261019_135940_grid/` (127 symbols x 66
pairs), 0 blocked, 8,379 rejected, 3 exploratory in the scan (JASMY P20_200, JASMY P21_200,
SUPER P8_200) - all 3 rejected by OOS + cost stress, so **0 credible candidates**. Pooled
mean net PF 0.4823, median 0.5037, best 1.0377 (SUPER/USDT P8_200), 6,918,813 trades.
Cells with net PF > 1: 3 / 8,382 = 0.04 % against a ~50 % no-edge null. Batch 12 alone:
660 cells, 660 rejected, mean net PF 0.5010, best 0.9717. Batch 12 is DONE - the six
names that had failed with KuCoin `400100` last session were transient API errors and
were fetched cleanly on retry (no name was dropped).

DO NEXT (batch 13, N 127 -> 137):
1. Fresh ranking + expansion: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 4
   --batch-size 10` (dry run), then `--apply-from universe/mcap_snapshot_<TS>.json
   --batch-size 10 --apply`. Expected next 10: KSM, NMR, YFI, HNT, ORDI, KAVA, AMP, DUSK,
   CKB, VELO (re-check on the fresh fetch; keep the order strictly market-cap descending).
2. OHLCV: `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10>`,
   then `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest`.
   If a symbol returns KuCoin `400100`, RE-QUERY it before treating it as ineligible -
   that error was transient for all six batch-12 names.
3. Grid, one invocation per symbol, checkpoint after each:
   `PYTHONPATH=. python3 scripts/run_grid.py --n 128` ... `--n 137` with
   `--resume results/20261019_135940_grid --note "universe expansion batch 13: N 127 -> 137 (<SYMBOL>/USDT, 66-pair EMA grid)"`,
   then `PYTHONPATH=. python3 scripts/remote_checkpoint.py --message "chore(kilo): grid batch13 <SYMBOL>/USDT (66 cells, N=137)" --paths results/20261019_135940_grid`.
4. `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid`
   then `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid`.
5. Append the batch-13 section to `universe/mcap_expansion_log.md` (+ row in the
   "Grid coverage per batch" table), update `NEXT_AGENT_TASK.md` and this file, checkpoint.

RULES: never promote a cell on in-sample numbers alone (PROMPT.md §3.3 - OOS + 2x cost
stress are required); keep the universe append-only and strictly market-cap descending; do
not stand down after a failed batch (PROMPT.md §2.1.4).

Environment: `PYTHONPATH=. python3` (pandas/numpy/pytest/requests are installed; if not:
`python3 -m pip install --break-system-packages pandas numpy pytest`).

Validation: `python -m pytest tests/ -q` (46 passing at handoff).
