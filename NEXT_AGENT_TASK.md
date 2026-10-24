# NEXT AGENT TASK — Durable Handoff (verified 2026-10-24T17:07:08Z; gate eligible=False, bound NOT yet elapsed)
1:
2: ## Current state
3: - State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`
4: - Offline gate re-verified 2026-10-24T17:07:08Z: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed (~21.6h remaining); no provider contact made. Nothing actionable until the bound. No provider call was made in this session.
5: - Universe: **N = 275** symbols (BTC/USDT ... ALPINE/USDT), ranked strictly market-cap descending, append-only.
6: - Baseline grid: `results/20261019_135940_grid` — **18 150/18 150 cells complete** (275 × 66 EMA pairs), `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, `stop_reason=null`, `completed_cells=18150 == n_symbols(275) x n_pairs(66)`, 0 blocked. `progress.json` has no "blocked" substring.
7: - `summary.json` pooled: n_cells 18150, n_symbols 275, n_pairs 66, total_trades 14 676 563, mean_net_pf 0.4987, median 0.5198, best_net_pf 2.2274, n_cells_net_pf_gt_1 37, n_exploratory_signal 27, n_rejected 18123, n_blocked 0, credible candidates 0.
8: - Last scan (Batch 29): `universe/mcap_snapshot_20261024_143039.json` (2026-10-24T14:30:39.449637Z, 20/20 pages, 2 000 entries, lowest covered $3 363 414). Floor `CWEB/USDT` $3 388 825. `eligible_unseen_below_floor_count = 0`. Coverage reaches below the floor ($3 363 414 < $3 388 825), so the band was genuinely inspected — not an incomplete scan. The 7 entries below the floor are all ineligible (7 no tradable KuCoin spot USDT pair; 0 history-probe failures). State set back to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next bound `2026-10-25T14:30:39.449637Z`.
9: - Refresh bound: **2026-10-25T14:30:39.449637Z** (not yet elapsed as of 2026-10-24T17:07:08Z). ~21.6h remaining.
10:
11: ## Your task (run at/after 2026-10-25T14:30:39.449637Z)
12: **Do NOT** contact CoinGecko/KuCoin before that timestamp.
13:
14: 1. Verify eligibility offline:
15:    ```bash
16:    PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
17:    ```
18:    Must return `eligible: True`. If `False`, stop and report the bound — nothing is actionable.
19:
20: 2. Run exactly one 20-page ranking pass (the only provider contact this cycle):
21:    ```bash
22:    PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
23:    ```
24:
25: 3. Re-check `eligible_unseen_below_floor_count` against the new floor.
26:
27: 4. **If candidates exist:** append descending market-cap names, log to `universe/mcap_expansion_log.md` (previous N → new N, rank range, source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, run the full 66-pair EMA grid per new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`, then `scripts/aggregate_grid.py` and `scripts/candidate_check.py`. Never create a second writer on the baseline grid; never promote from a partial child grid.
28:
29: 5. **If no candidates exist:** record the pass in `universe/mcap_expansion_log.md` (snapshot_id, fetch time, pages, floor, exclusions), set `universe/last_scan.json` state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, and set the next bound to +24 h from the new scan time.
30:
31: 6. Update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the new bound and the next unprocessed symbol/pair batch (or "none").
32:
33: ## Next unprocessed symbol/pair batch
34: - None. Awaiting new eligible names from the next 20-page pass at/after the bound.
35:
36: ## Constraints
37: - No provider call before 2026-10-25T14:30:39.449637Z.
38: - No second writer on `results/20261019_135940_grid`; no promotion from a partial child grid.
39: - No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
40: - Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`).
41: - Do not stop the program on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7.
42: - `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is a pre-existing clock-relative bug — do not loosen the gate.
43: - Wakeup at 2026-10-25T14:31:00Z scheduled to resume this task at the bound; do not re-schedule a duplicate.
44:
45: (End of file - total 46 lines)
