# NEXT AGENT TASK — Durable Handoff (re-verified 2026-10-25T13:45:47Z)

## Turn 2026-10-25T13:45:47Z verification (no provider contact)
- Offline gate re-checked: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed (`now` 2026-10-25T13:45:47.596122+00:00`). Nothing actionable until the bound elapses.
- No provider contact made. Baseline grid unchanged: 275x66, 0 credible candidates (18150 completed cells).
- Session prep: `git status --short` empty, `git diff --stat` empty.
- Wakeup state: resume wakeup previously scheduled at `2026-10-25T14:29:21.500Z` (`wku_1734639b80012EHAn8yk1EMzzC`) carrying the full resume prompt. Do not create a duplicate.
- Universe state unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next bound `2026-10-25T14:30:39.449637+00:00`.

## Current state
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES` (Batch 29 done 2026-10-24T14:30:39Z)
- Offline gate re-verified **2026-10-25T13:45:47.596122+00:00**:
  `{'eligible': False, 'bound': '2026-10-25T14:30:39.449637+00:00', 'now': '2026-10-25T13:45:47.596122+00:00', 'reason': 'the 24 h refresh bound 2026-10-25T14:30:39.449637+00:00 has not elapsed yet'}`.
- Nothing is actionable until the bound elapses; **no provider contact was made this turn**.
- Baseline grid re-verified via `results/20261019_135940_grid/progress.json`: 275x66, all processed, 0 blocked, 0 credible candidates.
- Universe: **N = 275** symbols (BTC/USDT ... ALPINE/USDT), ranked strictly market-cap descending. `universe/mcap_rank.json` updated_at `2026-10-22T12:15:58.878331+00:00`. Last scan `universe/mcap_snapshot_20261024_143039.json` (2026-10-24T14:30:39.449637Z), floor `CWEB/USDT` 3 388 825 USD, `eligible_unseen_below_floor_count = 0`. Next bound `2026-10-25T14:30:39.449637+00:00`.

## Your task (run at/after 2026-10-25T14:30:39.449637+00:00)
**Do NOT** contact CoinGecko/KuCoin before that timestamp. A resume wakeup (`wku_1734639b80012EHAn8yk1EMzzC`) is scheduled for `2026-10-25T14:29:21.500Z` to execute the pass automatically; if the session resumes before then, do not create a second wakeup and do not contact the provider before the bound.

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
- None. Awaiting new eligible names from the next 20-page pass at/after the bound `2026-10-25T14:30:39.449637+00:00`. A resume wakeup (`wku_1734639b80012EHAn8yk1EMzzC`) is scheduled for `2026-10-25T14:29:21.500Z` to execute the pass automatically; if the session resumes before then, do not create a second wakeup and do not contact the provider before the bound.

## Constraints
- No provider call before `2026-10-25T14:30:39.449637+00:00`.
- No second writer on `results/20261019_135940_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`).
- Do not stop the program on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7.
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is a pre-existing clock-relative bug — do not loosen the gate.
