# How this artifact was built

The grid-wide null leg was **not** recomputed. The three null modes
(`block`, `timing`, `sign`) of the 17 556 cells were already computed in
`results/20261021_073300_null_grid_scan/`; that checkpoint was copied here
unchanged, so `scripts/null_grid_scan.py` resumed on it ("Resuming: 17556
cells already checkpointed, 0 cells still to run") and only the survivor leg
and the harness validation were computed.

`survivor_source/cells.jsonl` is the survivor set, filtered out of
`results/20261021_033523_oos_grid_scan/cells.jsonl`: the cells with at least 30
out-of-sample trades, an out-of-sample net PF above 1 **and** an out-of-sample
net PF still above 1 under the 2x cost stress. That is 10 cells:

| Symbol | Cell | OOS trades | OOS net PF | OOS 2x-cost net PF |
|---|---|---|---|---|
| BRETT/USDT | P8_200 | 51 | 1.3107 | 1.0111 |
| DEXE/USDT | P12_200 | 79 | 1.2103 | 1.0325 |
| DEXE/USDT | P20_200 | 77 | 1.4790 | 1.2967 |
| DEXE/USDT | P21_200 | 75 | 1.4985 | 1.3136 |
| DEXE/USDT | P26_200 | 73 | 1.1484 | 1.0066 |
| DEXE/USDT | P50_200 | 86 | 1.3565 | 1.1165 |
| DEXE/USDT | P55_200 | 81 | 1.3378 | 1.0789 |
| GRT/USDT | P20_200 | 61 | 1.4547 | 1.2401 |
| GRT/USDT | P8_200 | 64 | 1.3136 | 1.0548 |
| MERL/USDT | P8_200 | 31 | 1.2518 | 1.0215 |

The filter is a plain read of the audit artifact:

```python
for row in json.load(open('results/20261021_033523_oos_grid_scan/cells.jsonl')):
    if (row['oos_trades'] or 0) >= 30 \
            and (row['oos_net_pf'] or 0.0) > 1.0 \
            and (row['oos_stress_net_pf'] or 0.0) > 1.0:
        keep(row)
```

`scripts/null_grid_scan.py --survivors-from` re-reads this file with the same
predicate (`oos_trades >= min_trades` and `oos_net_pf > 1.0`), so every row
kept here is re-randomized.

Command:

```
PYTHONPATH=. python3 scripts/null_grid_scan.py \
  --run results/20261019_135940_grid \
  --out results/20261021_104104_null_survivor_scan \
  --modes block timing sign \
  --survivors-from results/20261021_104104_null_survivor_scan/survivor_source \
  --survivor-modes timing block sign \
  --survivor-replicates 60 --control-sample 12 --validate-sample 24 --workers 4
```

The null of a cell is a deterministic function of the cell identity and the
mode (`null_grid_scan.cell_seed`), so re-running the leg reproduces the same
numbers.
