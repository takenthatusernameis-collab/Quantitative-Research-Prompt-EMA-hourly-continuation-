# NEXT AGENT TASK — Durable Handoff (re-verified 2026-10-24T10:00:16 UTC; gate eligible=False, bound not elapsed)
## Current state
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- Universe: **N = 275** symbols (BTC/USDT ... ALPINE/USDT), ranked strictly market-cap descending, append-only.
- Baseline grid: `results/20261019_135940_grid` — **18 150/18 150 cells complete** (275 × 66 EMA pairs), `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, `stop_reason=null`, `completed_cells=18150 == n_symbols(275) x n_pairs(66)`, 0 blocked. `progress.json` has no "blocked" substring.
- `summary.json` pooled: n_cells 18150, n_symbols 275, n_pairs 66, total_trades 14 676 563, mean_net_pf 0.4987, median 0.5198, best_net_pf 2.2274, n_cells_net_pf_gt_1 37, n_exploratory_signal 27, n_rejected 18123, n_blocked 0, credible candidates 0.
- Last scan: batch 28, `universe/mcap_snapshot_20261023_122828.json` (2026-10-23T12:28:28.949476Z, 20/20 pages, 2 000 entries, lowest covered $3 441 774). Floor `BOSON/USDT` $3 558 643. `eligible_unseen_below_floor_count = 0`. Coverage reaches below the floor ($3 441 774 < $3 558 643), so the band was genuinely inspected — not an incomplete scan. The 21 entries below the floor are all ineligible (18 no tradable KuCoin spot USDT pair; 3 fail the 2-year hourly-history probe).
- Refresh bound: **2026-10-24T12:28:28.949476Z** (~2h 34m remaining from 09:54:32Z).
- **This session (2026-10-24T10:00:16Z): re-verified the gate offline** — `gate_status` returned `eligible: False`, bound `2026-10-24T12:28:28.949476+00:00`, now `2026-10-24T10:00:16.202404+00:00`, reason "the 24 h refresh bound ... has not elapsed yet". **No provider contact made.** Nothing actionable until the bound elapses. Baseline grid independently re-verified: 18150/18150 cells, 0 blocked, internally consistent. Wakeup `wku_16d55e7cb001XsXtCCDc2pvwQX` scheduled at 2026-10-24T12:29:00Z to execute the refresh pass.

## Your task (run at/after 2026-10-24T12:28:28.949476Z)
**Do NOT** contact CoinGecko/KuCoin before that timestamp.

1. Verify eligibility offline:
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report the bound — nothing is actionable.

2. Run exactly one 20-page ranking pass (the only provider contact this cycle):
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```

3. Re-check `eligible_unseen_below_floor_count` against the new floor.

4. **If candidates exist:** append descending market-cap names, log to `universe/mcap_expansion_log.md` (previous N → new N, rank range, source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, run the full 66-pair EMA grid per new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`, then `scripts/aggregate_grid.py` and `scripts/candidate_check.py`. Never create a second writer on the baseline grid; never promote from a partial child grid.

5. **If no candidates exist:** record the pass in `universe/mcap_expansion_log.md` (snapshot_id, fetch time, pages, floor, exclusions), set `universe/last_scan.json` state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, and set the next bound to +24 h from the new scan time.

6. Update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the new bound and the next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. Awaiting new eligible names from the next 20-page pass at/after the bound.

## Constraints
- No provider call before 2026-10-24T12:28:28.949476Z.
- No second writer on `results/20261019_135940_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`).
- Do not stop the program on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7.
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is a pre-existing clock-relative bug — do not loosen the gate.
- Wakeup `wku_16d55e7cb001XsXtCCDc2pvwQX` at 2026-10-24T12:29:00Z executes the refresh pass; do not re-schedule a duplicate.
