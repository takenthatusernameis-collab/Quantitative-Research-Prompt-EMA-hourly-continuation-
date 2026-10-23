# Initial task for the next agent — stricter-trend single-variable mutation of the expanded baseline

## Situation (verified 2026-10-23T01:33:12Z)

- Expansion complete: N = 275, floor `ALPINE/USDT` $3 614 141, snapshot `universe/mcap_snapshot_20261022_121558.json` (fetched 2026-10-22T12:15:58Z).
- Baseline grid `results/20261019_135940_grid`: 275 symbols × 66 pairs = 18 150 cells, complete, 0 blocked. Aggregate mean net PF 0.4993; candidate_check rejected all; tests **249 passed**.
- State `MUTATION_RUNNING`; next eligible universe refresh **2026-10-23T12:15:58Z** — **no provider contact before then**.
- ATR min-risk mutation is closed (`NOT_PROMOTED`, see `results/mutations.json`).
- Environment provisioned: pandas 3.1.0 + pytest 9.1.1 installed; `PYTHONPATH=. python3 -m pytest tests/ -q` → 249 passed.

## Task in progress (resume / monitor this first)

A stricter-trend single-variable mutation of the expanded baseline is running as a persistent background process:

- Run dir: `results/20261022_134500_grid` (`stricter_trend: true`; everything else — costs 10/2 bps, rr 1.0, conservative exit, risk sizing, folds, entry/exit, §3.4 gates — unchanged; ATR stays closed).
- Background writer: `bgp_166a765e3001uxvePsnTc6qHJQ` (pid 7254 + 4 workers), **persistent**, sole writer. Do **not** start a second writer on this run directory.
- Progress: 12 474 / 18 150 cells on disk (~5 676 remaining across ~86 symbols); next cell `MEW/USDT P8_12`; `stopped=true`, `stop_reason=in_progress`, `all_symbols_processed=false`. The grid runs across sessions (several hours of wall clock remaining). Writer last seen at `MOODENG/USDT: 66 cell(s) done, 12474/18150 total`.

Resume command (repository root; resumable — skips cells whose `summary.json` already exists):

```bash
PYTHONPATH=. python3 scripts/run_mutation_grid.py --run results/20261022_134500_grid --stricter-trend --workers 4 --parent-run results/20261019_135940_grid
```

Check `background_process status bgp_165c26e18001HrFOj1yrcSOD6T` and `logs bgp_165c26e18001HrFOj1yrcSOD6T` before re-invoking. Only re-invoke if the writer is not running. Record `next_cell` from `results/20261022_134500_grid/progress.json` at each stop. Mutate **one variable at a time** (`stricter_trend` only).

## Once the mutation grid completes (`next_cell = null`)

Run the evaluation legs against child `results/20261022_134500_grid` vs parent `results/20261019_135940_grid`:

```bash
PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/mutation_eval.py --child results/20261022_134500_grid --parent results/20261019_135940_grid
PYTHONPATH=. python3 scripts/null_grid_scan.py --run results/20261022_134500_grid    # child's own randomized null
PYTHONPATH=. python3 scripts/mutation_repro_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/mutation_survivor_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 -m pytest tests/ -q
```

Then record a `NOT_PROMOTED`/promoted `decision` for child `C_stricter_trend` in `results/mutations.json` (`status = complete` with progress), close this child entry, and update `NEXT_AGENT_TASK.md` (and this file) with the outcome and the next task.

## Must not

- No provider (CoinGecko/KuCoin) call before 2026-10-23T12:15:58Z; the mutation work itself is offline.
- No re-run of the baseline grid; no second writer on `results/20261022_134500_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables in this run (`--min-risk-atr`, `--rr`, `--aggressive-exit` stay out).

(End of file)
