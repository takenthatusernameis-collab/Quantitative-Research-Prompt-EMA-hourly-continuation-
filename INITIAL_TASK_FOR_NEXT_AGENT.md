# NEXT TASK — refresh bound 2026-10-24T12:28:28.949476Z (verified 2026-10-24T04:26 UTC)

## Initial task message for the next agent
The program is in `AWAITING_NEW_ELIGIBLE_CANDIDATES` after batch 28 (2026-10-23T12:28:28Z pass found 0 eligible unseen names below the floor; 2000-entry CoinGecko ranking band exhausted down to $3,441,774). Universe n=275. The 24h refresh bound expires at 2026-10-24T12:28:28.949476Z. **Do not** contact CoinGecko/KuCoin before that timestamp.

Offline check confirmed (2026-10-24T04:31:39Z): `eligible: False`, bound `2026-10-24T12:28:28.949476+00:00`, now `2026-10-24T04:31:39+00:00`. Reason: bound not elapsed (~7h 57m remaining). No provider contact made. State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=275`, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`. Baseline grid `results/20261019_135940_grid` verified complete (18150/18150 cells, 275 symbols × 66 pairs, `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, 0 blocked — `completed` list length 18150, no "blocked" substring anywhere in `progress.json`).

A wakeup is scheduled for 2026-10-24T12:28:29Z (id `wku_16c293ecb001w4pZDAt8TyUu1R`) to resume automatically. If harness does not resume, run steps below at/after bound.

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

4. **If candidates exist:** expand per PROMPT.md §2.1 — append descending market-cap candidates (track previous→new N, rank range, log to `universe/mcap_expansion_log.md` with source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, run full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`. Never create second writer on baseline grid; never promote from partial child grid.

5. **If no candidates exist:** record pass (snapshot_id, fetch time, pages, floor, exclusions) in `universe/mcap_expansion_log.md`, set `universe/last_scan.json` state to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next bound becomes +24h from new scan time.

6. **Update handoffs:** after completing (or determining no-candidates), update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with new bound and next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. No candidates exist; awaiting new eligible names from next 20-page pass at/after bound.

## Constraints
- No provider call before 2026-10-24T12:28:28.949476Z
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`)
- Do not stop on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7
- Tests: `pytest` not importable in prior sessions; confirm env before relying on 248/249 figure. `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is pre-existing clock-relative bug — do not loosen gate.

(End of file - total 40 lines)