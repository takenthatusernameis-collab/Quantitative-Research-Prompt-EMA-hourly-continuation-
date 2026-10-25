# NEXT AGENT TASK — Durable Handoff (re-verified 2026-10-25T15:42:37+00:00)

## Turn 2026-10-25T15:42:37+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T15:42:37.568355+00:00`).
- No provider contact. `universe/last_scan.json` unchanged.
- Tests: 248 passed, 1 failed (pre-existing clock bug `tests/test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`).
- `git status --short` empty, `git diff --stat` empty.

## Current state
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES` (Batch 30 done 2026-10-25T15:14:53Z)
- Last scan: `universe/mcap_snapshot_20261025_151453.json` (2026-10-25T15:14:53.192289Z)
- Coverage: 2000 entries down to rank 2000 (~$3,338,115), coverage_reaches_below_floor true.
- Universe: **N = 275** symbols (BTC/USDT ... ALPINE/USDT), floor `ALPINE/USDT` $3,405,003. `eligible_unseen_below_floor_count = 0`.
- Next bound: `2026-10-26T15:14:53.192289+00:00`.
- Baseline grid `results/20261019_135940_grid`: 275x66, all processed, 0 blocked, 0 credible candidates.

## Your task (run at/after 2026-10-26T15:14:53.192289+00:00)
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

4. **If candidates exist:** append descending market-cap names, log to `universe/mcap_expansion_log.md` (previous N -> new N, rank range, source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, run the full 66-pair EMA grid per new symbol with:
   ```bash
   PYTHONPATH=. python3 scripts/run_grid.py --mcap universe/mcap_rank.json --n <NEW_TOTAL_N> --fixture-base data/fixtures --resume results/20261019_135940_grid
   ```
   (`--n` is the new total N, not the default 5; resume skips already-completed cells.) Then `scripts/aggregate_grid.py --run results/20261019_135940_grid` and `scripts/candidate_check.py --run results/20261019_135940_grid`. Never create a second writer on the baseline grid; never promote from a partial child grid.

5. **If no candidates exist:** record the pass in `universe/mcap_expansion_log.md` (snapshot_id, fetch time, pages, floor, exclusions), set `universe/last_scan.json` state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, and set the next bound to +24 h from the new scan time.

6. Update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the new bound and the next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. No eligible unseen names below floor found in 2026-10-25T15:14:53 pass (2000 entries down to ~$3.34M). Awaiting next pass at/after `2026-10-26T15:14:53.192289+00:00`.

## Constraints
- No provider call before `2026-10-26T15:14:53.192289+00:00` (the 24 h refresh bound).
- No second writer on `results/20261019_135940_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`).
- Do not stop the program on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7.
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is a pre-existing clock-relative bug — do not loosen the gate.
