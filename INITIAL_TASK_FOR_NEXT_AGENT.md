# INITIAL TASK MESSAGE FOR NEXT AGENT (re-verified 2026-10-25T15:14:53+00:00)

## Turn 2026-10-25T15:14:53+00:00 (completed)
- Gate was open at execution time; ran 20-page pass (only provider contact this cycle). CoinGecko had retries but completed.
- Snapshot: `universe/mcap_snapshot_20261025_151453.json` (2000 entries, pages 20/20, lowest covered rank 2000 ~$3,338,115).
- Coverage reaches below floor true; floor now `ALPINE/USDT` $3,405,003.
- **Eligible unseen below floor: 0** (no candidates). Dry run only — no universe expansion applied, no grid runs.
- `universe/last_scan.json` updated: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next eligible refresh `2026-10-26T15:14:53.192289+00:00`.
- Baseline grid `results/20261019_135940_grid` unchanged: 275x66, 0 credible candidates.

## Context
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES` (Batch 30 done 2026-10-25T15:14:53Z). 2000-entry band exhausted down to ~3.34M; no eligible unseen names below current floor. Universe N=275.
- Next bound: `2026-10-26T15:14:53.192289+00:00`.
- Baseline grid has 0 credible candidates (275x66, 18150 completed cells, 0 blocked).

## Required action (at/after bound 2026-10-26T15:14:53.192289+00:00)
**Do NOT** contact CoinGecko/KuCoin before `2026-10-26T15:14:53.192289+00:00`.

1. **Verify eligibility offline first:**
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report bound; nothing actionable.

2. **Run exactly one 20-page market-cap ranking pass** (the only provider contact this cycle):
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```
   Freezes snapshot for 24h and writes new bound to `universe/last_scan.json`.

3. **Re-check band below current floor** for `eligible_unseen_below_floor_count`.

4. **If candidates exist:** expand per PROMPT.md §2.1 — append descending market-cap candidates, log to `universe/mcap_expansion_log.md` with source/date, fetch OHLCV via `scripts/fetch_kucoin.py`, run full 66-pair EMA grid on each new symbol with:
   ```bash
   PYTHONPATH=. python3 scripts/run_grid.py --mcap universe/mcap_rank.json --n <NEW_TOTAL_N> --fixture-base data/fixtures --resume results/20261019_135940_grid
   ```
   Then `scripts/aggregate_grid.py --run results/20261019_135940_grid` and `scripts/candidate_check.py --run results/20261019_135940_grid`. Never create second writer on baseline grid; never promote from partial child grid.

5. **If no candidates exist:** record pass in `universe/mcap_expansion_log.md` (snapshot_id, fetch time, pages, floor, exclusions), set `universe/last_scan.json` state to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next bound becomes +24h from new scan time.

6. **Update handoffs:** update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with new bound and next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. No candidates in 2026-10-25T15:14:53 pass; awaiting new eligible names from next pass at/after `2026-10-26T15:14:53.192289+00:00`.

## Constraints
- No provider contact before `2026-10-25T14:30:39.449637+00:00`
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables
- Do not stop on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is pre-existing clock-relative bug — do not loosen gate.
