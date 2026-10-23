# INITIAL TASK FOR NEXT AGENT

Run at/after 2026-10-24T12:28:28.949476Z (refresh bound). Do NOT contact the provider before that timestamp.

1. Verify eligibility offline first: `PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"` → must return `eligible: True`.
2. Run exactly one 20-page market-cap ranking pass: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`.
3. Freeze the new snapshot for 24 h.
4. Re-check the band below the current floor for eligible unseen candidates.
5. If candidates exist, expand the universe per PROMPT.md §2.1 (append next lower market-cap candidates, descending order; previous N → new N, rank range added, source/date in `universe/mcap_expansion_log.md`) and run the full 66-pair EMA grid on each new symbol.
6. Log the pass in `universe/mcap_expansion_log.md`.
7. Update `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`.

Program state: N=275, floor BOSON/USDT $3 558 643 (recomputed from the 2026-10-23T12:28:28Z snapshot), baseline grid `results/20261019_135940_grid` (18 150/18 150 cells, 0 blocked), null scan complete (no edge), both mutations NOT_PROMOTED, batch 28 logged (no new candidates). No provider contact before the bound.

## Verification performed 2026-10-23T13:49 UTC (this session)

- `gate_status(universe/last_scan.json)` → `eligible: False`, bound 2026-10-24T12:28:28.949476+00:00, now 2026-10-23T13:49:31Z. No provider contact made.
- `universe/last_scan.json`: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, universe_n 275, eligible_unseen_below_floor_count 0, batch_selected [], snapshot `universe/mcap_snapshot_20261023_122828.json` frozen, next_eligible_refresh_at 2026-10-24T12:28:28.949476+00:00.
- Baseline grid `results/20261019_135940_grid/progress.json`: completed_cells 18 150 (= 275 symbols × 66 pairs), all_symbols_processed true, next_cell null. `summary.json`: n_cells 18 150, n_symbols 275, n_pairs 66, mean_net_pf 0.4987, n_cells_net_pf_gt_1 37, n_exploratory_signal 27, n_rejected 18 123, n_blocked 0.
- `results/mutations.json`: `C_stricter_trend` (zero-delta no-op, NOT_PROMOTED, decided 2026-10-23T05:30:00Z) and `C_min_risk_atr` (NOT_PROMOTED, decided 2026-10-22T02:55:00Z) both closed. Baseline grid remains the program grid.
- Null grid scan `results/20261023_050716_null_grid_scan/summary.md`: 18 150 cells; real 77 cells OOS net PF > 1 / 6 gate-clearing vs block null 320 / 24, timing 86 / 7, sign 44 / 1; pooled OOS net PF real 0.4163 vs nulls 0.4480-0.5114; best real 1.4697 vs best block 2.2215; Leg 0 harness 200/200. Conclusion: no edge.
- `universe/mcap_expansion_log.md`: batch 28 (refresh pass 2026-10-23T12:28:28Z, no eligible name below floor, universe unchanged at N=275) recorded; Batch 27 (N 266 → 275, BLZ/PIXEL/ALEX/CWEB/TRADE/ZPAY/ZKJ/BOSON/ALPINE) recorded.
- Environment: `/usr/bin/python3` — numpy 2.5.4, pandas 3.1.0 present; `pytest` not installed.

Nothing further is actionable before the bound. Next agent runs at/after 2026-10-24T12:28:28.949476Z.

## Verification performed 2026-10-23T13:55 UTC (this session)

- `gate_status(universe/last_scan.json)` → `eligible: False`, bound 2026-10-24T12:28:28.949476+00:00, now 2026-10-23T13:55:59Z. No provider contact made.
- `universe/last_scan.json`: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, universe_n 275, eligible_unseen_below_floor_count 0, batch_selected [], snapshot `universe/mcap_snapshot_20261023_122828.json` (on disk, 12:28 UTC, frozen), next_eligible_refresh_at 2026-10-24T12:28:28.949476+00:00. Coverage 20 pages / 2 000 entries / lowest $3 441 774, below the floor ($3 558 643).
- Baseline grid `results/20261019_135940_grid`: `progress.json` completed_cells 18 150 (= 275 symbols × 66 pairs), `all_symbols_processed` true, `next_cell` null, `stopped` false. `summary.json` → n_cells 18 150, n_symbols 275, n_pairs 66, total_trades 14 676 563, mean_net_pf 0.4987, median 0.5198, best_net_pf 2.2274, n_cells_net_pf_gt_1 37, n_exploratory_signal 27, n_rejected 18 123, n_blocked 0. `per_symbol.json` = 275 records; batch-27 additions BLZ/PIXEL/ALEX/CWEB/TRADE/ZPAY/ZKJ/BOSON/ALPINE all present.
- `results/mutations.json`: `C_stricter_trend` (zero-delta no-op, NOT_PROMOTED, decided 2026-10-23T05:30:00Z) and `C_min_risk_atr` (NOT_PROMOTED, decided 2026-10-22T02:55:00Z) both closed. Baseline grid remains the program grid.
- Null grid scan `results/20261023_050716_null_grid_scan/summary.md`: 18 150 cells; real 77 cells OOS net PF > 1 / 6 gate-clearing vs block null 320 / 24, timing 86 / 7, sign 44 / 1; pooled OOS net PF real 0.4163 vs nulls 0.4480-0.5114; best real 1.4697 vs best block 2.2215; Leg 0 harness 200/200. Conclusion: no edge.
- `universe/mcap_expansion_log.md`: Batch 28 (refresh pass 2026-10-23T12:28:28Z, no eligible name below floor, universe unchanged at N=275) recorded; Batch 27 (N 266 → 275, BLZ/PIXEL/ALEX/CWEB/TRADE/ZPAY/ZKJ/BOSON/ALPINE) recorded.
- Environment: `/usr/bin/python3` — numpy 2.5.4, pandas 3.1.0 present; `pytest` not installed.

Nothing further is actionable before the bound. Next agent runs at/after 2026-10-24T12:28:28.949476Z.

## Verification performed 2026-10-23T14:00 UTC (this session)

- `gate_status(universe/last_scan.json)` → `eligible: False`, bound 2026-10-24T12:28:28.949476+00:00, now 2026-10-23T14:01:03Z. No provider contact made.
- `universe/last_scan.json`: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, universe_n 275, eligible_unseen_below_floor_count 0, batch_selected [], snapshot `universe/mcap_snapshot_20261023_122828.json` frozen, next_eligible_refresh_at 2026-10-24T12:28:28.949476+00:00. Coverage lowest $3 441 774 below the floor ($3 558 643).
- Baseline grid `results/20261019_135940_grid/progress.json`: completed_cells 18 150 (= 275 symbols × 66 pairs), all_symbols_processed true, next_cell null, stopped false. `summary.json` pooled mean net PF 0.4987, median 0.5198, best_net_pf 2.2274, n_cells_net_pf_gt_1 37, n_rejected 18 123, n_blocked 0.
- `results/mutations.json`: `C_stricter_trend` (zero-delta no-op, NOT_PROMOTED) and `C_min_risk_atr` (NOT_PROMOTED) both closed. Baseline grid remains the program grid.
- Null grid scan `results/20261023_050716_null_grid_scan/summary.md`: no edge (real 77 vs block null 320 OOS net PF > 1; pooled real 0.4163 vs nulls 0.4480-0.5114; Leg 0 harness 200/200).
- Environment: `/usr/bin/python3` — numpy 2.5.4, pandas 3.1.0 present; `pytest` not installed.

Nothing further is actionable before the bound. Next agent runs at/after 2026-10-24T12:28:28.949476Z.
