# INITIAL TASK MESSAGE FOR NEXT AGENT (re-verified 2026-10-25T13:29:05Z)

## Turn 2026-10-25T13:29:05Z verification (no provider contact)
- Offline gate: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed (`now` 2026-10-25T13:29:06.487668+00:00`). Nothing actionable.
- No provider contact made. Baseline grid unchanged; 0 credible candidates.
- Git status clean (`git status --short` empty, `git diff --stat` empty).
- Wakeup state: prior resume wakeup `wku_1732c01a90019wGSqrFeF9efkD` no longer pending (fired/resolved). New resume wakeup scheduled at 2026-10-25T14:29:21.500Z (`wku_17340615f001QnXQz8RUoU0tqd`) carrying the full resume prompt. Do not create a duplicate.

## Turn 2026-10-25T13:26:05Z verification (no provider contact)
- Offline gate: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed (`now` 2026-10-25T13:26:05.923187+00:00). Nothing actionable.
- No provider contact made. Baseline grid unchanged; 0 credible candidates.
- Git status clean. Single pre-existing test failure unchanged (pytest unavailable in this env).
- Resume wakeup `wku_1732c01a90019wGSqrFeF9efkD` at 2026-10-25T14:31:00.000Z; do not duplicate.

## Turn 2026-10-25T13:22:17Z verification (no provider contact)
- Offline gate: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed. Nothing actionable.
- No provider contact made. Baseline grid unchanged; 0 credible candidates.
- Git status clean. Resume wakeup `wku_1732c01a90019wGSqrFeF9efkD` at 2026-10-25T14:31:00.000Z; do not duplicate.

# INITIAL TASK MESSAGE FOR NEXT AGENT (re-verified 2026-10-25T13:21:44Z)

## Turn 2026-10-25T13:21:44Z verification (no provider contact)
- Offline gate: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed. Nothing actionable.
- No provider contact made. Baseline grid unchanged; 0 credible candidates.
- Git status clean. Single pre-existing test failure unchanged.
## Turn 2026-10-25T13:13:35Z verification (no provider contact)
- Offline gate: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed. Nothing actionable.
- Resume wakeup scheduled at 2026-10-25T14:35:56.965Z (`wku_17335ef6c001aaYCGg9j7g87qa`); do not duplicate.
- Baseline grid unchanged; 0 credible candidates.

## Turn 2026-10-25T13:04:15Z verification (no provider contact)
- Offline gate re-checked: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed (`now` 2026-10-25T13:04:15.983389+00:00`). Nothing actionable.
- Baseline grid `results/20261019_135940_grid/progress.json` re-read directly: `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, `stop_reason=null`, `completed_cells=18150` (275x66), 0 blocked. `summary.json.pooled`: n_cells 18150, n_symbols 275, n_pairs 66, total_trades 14676563, mean net PF 0.49869497744821545, median_net_pf 0.5197980508009844, best_net_pf 2.227366213741068, n_cells_net_pf_gt_1 37, n_exploratory_signal 27, n_rejected 18123, n_blocked 0, **0 credible candidates**.
- Session prep: `git status --short` empty, `git diff --stat` empty.
- Wakeup state: no pending wakeups at the start of this turn; a single resume wakeup was scheduled at 2026-10-25T14:31:00.000Z (`wku_1732c01a90019wGSqrFeF9efkD`) carrying the full resume prompt. Do not create a duplicate.
- Tests: `python -m pytest tests/ -q` -> 248 passed, 1 failed — the pre-existing clock-relative bug named in the handoff, `tests/test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`; left untouched.
- `universe/last_scan.json` re-read directly: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261024_143039`, scanned_at `2026-10-24T14:30:39.449637+00:00`, coverage 20/20 pages, 2000 entries, lowest_market_cap_usd 3363414, floor `CWEB/USDT` 3388825, `eligible_unseen_below_floor_count = 0`, `next_eligible_refresh_at` `2026-10-25T14:30:39.449637+00:00` — authoritative and unchanged.

## Turn 2026-10-25T12:59:49Z verification (no provider contact)
- Offline gate re-checked: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed (`now` 2026-10-25T12:59:49.473273+00:00`). Nothing actionable.
- Baseline grid `results/20261019_135940_grid/progress.json` re-read directly: `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, `stop_reason=null`, `completed_cells=18150` (275x66), 0 blocked. `summary.json.pooled`: n_cells 18150, n_symbols 275, n_pairs 66, total_trades 14676563, mean net PF 0.49869497744821545, median_net_pf 0.5197980508009844, best net PF 2.227366213741068, n_cells_net_pf_gt_1 37, n_exploratory_signal 27, n_rejected 18123, n_blocked 0, **0 credible candidates**.
- Session prep: `git status --short` empty, `git diff --stat` empty.
- Wakeup state: no pending wakeups for this session.
- Tests: `python -m pytest tests/ -q` -> 248 passed, 1 failed — the single failure is the pre-existing clock-relative bug named in the handoffs (`test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`), left untouched.

## Context
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES` (Batch 29 done 2026-10-24T14:30:39Z). Found 0 eligible unseen names below floor; 2000-entry CoinGecko band exhausted down to ~3388825. Universe N=275 (BTC/USDT ... ALPINE/USDT).
- Offline gate re-verified **2026-10-25T12:57:04.072636+00:00**: `{'eligible': False, 'bound': '2026-10-25T14:30:39.449637+00:00', 'now': '2026-10-25T12:57:04.072636+00:00', 'reason': 'the 24 h refresh bound 2026-10-25T14:30:39.449637+00:00 has not elapsed yet'}`.
- **No provider contact made this turn.** Nothing is actionable until the bound elapses.
- Baseline grid `results/20261019_135940_grid` has 0 credible candidates as above.

## Required action (at/after bound 2026-10-25T14:30:39.449637+00:00)
**Do NOT** contact CoinGecko/KuCoin before 2026-10-25T14:30:39.449637+00:00.
A resume wakeup (`wku_17340615f001QnXQz8RUoU0tqd`) is scheduled for 2026-10-25T14:29:21.500Z to execute this automatically; if the session resumes before then, do not create a second wakeup and do not contact the provider before the bound.

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
- None. No candidates exist currently; awaiting new eligible names from next 20-page pass at/after bound 2026-10-25T14:30:39.449637+00:00. The resume wakeup `wku_17340615f001QnXQz8RUoU0tqd` at 2026-10-25T14:29:21.500Z executes the pass automatically; do not create a second wakeup before the bound.

## Constraints
- No provider contact before 2026-10-25T14:30:39.449637+00:00
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables
- Do not stop on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is pre-existing clock-relative bug — do not loosen gate.
