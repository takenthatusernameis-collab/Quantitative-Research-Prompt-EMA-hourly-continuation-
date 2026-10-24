# NEXT TASK — refresh bound 2026-10-25T14:30:39.449637Z (verified 2026-10-24T15:27Z, gate eligible=False, bound not yet elapsed)

## Initial task message for the next agent

Offline gate re-verified 2026-10-24T15:27:48Z: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed (~23h remaining); no provider contact made. Nothing actionable until the bound.

The program is in `AWAITING_NEW_ELIGIBLE_CANDIDATES` after Batch 29 (2026-10-24T14:30:39Z pass found 0 eligible unseen names below the floor; 2000-entry CoinGecko ranking band exhausted down to $3,363,414). Universe n=275. The 24h refresh bound expires at 2026-10-25T14:30:39.449637Z. **Do not** contact CoinGecko/KuCoin before that timestamp.

Batch 29 results: snapshot `universe/mcap_snapshot_20261024_143039.json` (20/20 pages, 2000 entries), floor `CWEB/USDT` $3,388,825, `eligible_unseen_below_floor_count=0` (7 entries below floor all ineligible — no tradable KuCoin spot USDT pair). Coverage reached below floor. State set to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next bound +24h. No expansion applied, `universe/mcap_rank.json` unchanged.

Baseline grid re-verified: 18150/18150 cells complete (275 × 66), `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, `stop_reason=null`, 0 blocked. `summary.json` pooled: mean net PF 0.4987, median 0.5198, best net PF 2.2274, n_cells_net_pf_gt_1 37, n_rejected 18123, n_blocked 0, **0 credible candidates**.

## Steps
1. **Verify eligibility offline first:**
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report bound; nothing actionable.

2. **Run exactly one 20-page market-cap ranking pass:**
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```
   Only provider contact this cycle. Freezes snapshot for 24h and writes new bound to `universe/last_scan.json`.

3. **Re-check band below current floor** for `eligible_unseen_below_floor_count`.

4. **If candidates exist:** expand per PROMPT.md §2.1 — append descending market-cap candidates (track previous→new N, log to `universe/mcap_expansion_log.md` with source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, run full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`, then `scripts/aggregate_grid.py` and `scripts/candidate_check.py`. Never create second writer on baseline grid; never promote from partial child grid.

5. **If no candidates exist:** record pass (snapshot_id, fetch time, pages, floor, exclusions) in `universe/mcap_expansion_log.md`, set `universe/last_scan.json` state to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next bound becomes +24h from new scan time.

6. **Update handoffs:** after completing (or determining no-candidates), update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with new bound and next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. No candidates exist; awaiting new eligible names from next 20-page pass at/after bound 2026-10-25T14:30:39.449637Z.

## Constraints
- No provider call before 2026-10-25T14:30:39.449637Z
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`)
- Do not stop on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is pre-existing clock-relative bug — do not loosen gate.
- Wakeup `wku_16dcc65f9001i6INGKlOahwLY1` at 2026-10-24T12:29:00Z executed the refresh pass; do not re-schedule a duplicate.
