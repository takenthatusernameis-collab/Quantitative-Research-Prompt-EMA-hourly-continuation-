# NEXT AGENT TASK

## Objective
**Active / In progress.** Expand the EMA hourly-continuation research universe to the next lower market-cap batch (PROMPT.md §2.1) and run the full 66-pair EMA grid on the newly added symbols.

## Progress (2026-10-19)
- Full grid complete for all 5 ranked symbols (BTC, ETH, SOL, BNB, XRP): 5 × 66 = 330 cells, all net PF < 1 (rejected). Artifacts: `results/20261019_135940_grid/`.
- progress.json: `all_symbols_processed=true`, `next_cell=null`.
- Tests: `python -m pytest tests/ -q` → 17/17 pass.

## Next action
1. Obtain/extend market-cap ranking per §2.1 (descending mcap; document source, timestamp, rank drift).
2. Append next batch (5–20 names below XRP) to `universe/mcap_rank.json` with `updated_at`, snapshot id, added ranks.
3. Run full grid on newly added symbols only:
   `PYTHONPATH=. python scripts/run_grid.py --n <new_total> --taker-fee-bps 10 --slippage-bps 2 --rr 1.0`
   (resumes via progress.json).

## Constraints
- Do not invent symbols; market cap descending only.
- Do not delete prior artifacts.
- Continue after total failure; document cumulative rejection rate.

## Validation
`python -m pytest tests/ -q`
