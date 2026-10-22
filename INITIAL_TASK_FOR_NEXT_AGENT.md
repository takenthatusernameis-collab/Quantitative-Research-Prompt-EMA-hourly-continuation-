# Initial task for the next agent — stricter-trend single-variable mutation of the expanded baseline

## Situation (verified 2026-10-22T14:18Z)

- Expansion complete: N = 275, floor `ALPINE/USDT` $3 614 141, snapshot `universe/mcap_snapshot_20261022_121558.json`.
- Baseline grid `results/20261019_135940_grid`: 275 symbols × 66 pairs = 18 150 cells, complete, 0 blocked. Aggregate mean net PF 0.4987; candidate_check rejected all; tests **249 passed**.
- State `AWAITING_NEW_ELIGIBLE_CANDIDATES`; next eligible universe refresh **2026-10-23T12:15:58Z** — **no provider contact before then**.
- ATR min-risk mutation is closed (`NOT_PROMOTED`, see `results/mutations.json`).

## Task in progress (resume this first)

A stricter-trend single-variable mutation of the expanded baseline is running as a persistent background process:

`results/20261022_134500_grid` (`stricter_trend: true`; everything else — costs 10/2 bps, rr 1.0, conservative exit, risk sizing, folds, entry/exit, §3.4 gates — unchanged; ATR stays closed).

Progress: **1056 / 18 150 cells complete** (16 symbols done: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT, XRP/USDT, TRX/USDT, ZEC/USDT, DOGE/USDT, XMR/USDT, ADA/USDT, LINK/USDT, NEAR/USDT, XLM/USDT, BCH/USDT, LTC/USDT, UNI/USDT), next cell advancing past UNI/USDT.

Resume command (run from the repository root; it is resumable — skips cells whose `summary.json` already exists — do NOT start a second writer on this run directory):

```bash
PYTHONPATH=. python3 scripts/run_mutation_grid.py --run results/20261022_134500_grid --stricter-trend --workers 4 --parent-run results/20261019_135940_grid
```

The full grid needs ~9+ hours at the current rate (~2 min/symbol) and spans sessions. Record `next_cell` from `progress.json` at each stop. Mutate **one variable at a time** (`stricter_trend` only).

A wakeup is scheduled for 2026-10-22T15:22:38Z to check completion.

## Once the mutation grid completes (next_cell = null)

Run the evaluation legs against the child grid `results/20261022_134500_grid` vs parent `results/20261019_135940_grid`:

```bash
PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/mutation_eval.py --child results/20261022_134500_grid --parent results/20261019_135940_grid
PYTHONPATH=. python3 scripts/null_grid_scan.py --run results/20261022_134500_grid    # child's own randomized null
PYTHONPATH=. python3 scripts/mutation_repro_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/mutation_survivor_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 -m pytest tests/ -q
```

Then record a `NOT_PROMOTED`/promoted `decision` for child `C_stricter_trend` in `results/mutations.json`, close the entry, and update `NEXT_AGENT_TASK.md` (and this file) with the outcome and the next task.

## Must not

- No provider (CoinGecko/KuCoin) call before 2026-10-23T12:15:58Z; the mutation work itself is offline.
- No re-run of the baseline grid; no second writer on `results/20261022_134500_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables in this run (`--min-risk-atr`, `--rr`, `--aggressive-exit` stay out).
