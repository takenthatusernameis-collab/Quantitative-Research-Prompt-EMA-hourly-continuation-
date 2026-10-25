# NEXT AGENT TASK — Durable Handoff (re-verified 2026-10-25T16:59:31+00:00)

## Initial Task Message (read first)

**You are the next agent in the EMA hourly continuation research loop.** Your job is a single gated cycle of market-cap universe expansion. Everything you need is below; do not improvise beyond it.

**Current state:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Universe N=275 (BTC/USDT … ALPINE/USDT), floor ALPINE/USDT $3,405,003. Baseline grid `results/20261019_135940_grid` (275×66) is complete: 0 blocked, 0 credible candidates. Last scan `universe/mcap_snapshot_20261025_151453.json` covered 2000 entries down to rank 2000 (~$3.34M) with 0 eligible unseen names below floor.

**Your task, in order:**

1. **Wait for the gate.** Do NOT contact CoinGecko/KuCoin before `2026-10-26T15:14:53.192289+00:00`. Check eligibility offline first:
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report the bound — nothing is actionable. (This is exactly what the previous turn did; the gate was still closed as of 2026-10-25T15:48:49Z.)

2. **If eligible, run exactly one 20-page ranking pass** (the only provider contact this cycle):
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```

3. **Re-check `eligible_unseen_below_floor_count`** against the new floor.

4. **If candidates exist:** append descending market-cap names, log to `universe/mcap_expansion_log.md` (previous N → new N, rank range, source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, then run the full 66-pair EMA grid per new symbol with:
   ```bash
   PYTHONPATH=. python3 scripts/run_grid.py --mcap universe/mcap_rank.json --n <NEW_TOTAL_N> --fixture-base data/fixtures --resume results/20261019_135940_grid
   ```
   (`--n` is the new total N; `--resume` skips already-completed cells.) Then:
   ```bash
   PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid
   PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid
   ```
   Never create a second writer on the baseline grid; never promote from a partial child grid.

5. **If no candidates exist:** record the pass in `universe/mcap_expansion_log.md` (snapshot_id, fetch time, pages, floor, exclusions), set `universe/last_scan.json` state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, and set the next bound to +24 h from the new scan time.

6. **Update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`** with the new bound and the next unprocessed symbol/pair batch (or "none").

**Hard constraints:** no provider call before the bound; no second writer on the baseline grid; no partial-grid promotion; no changes to costs/folds/entry-exit/gates; do not combine variables; do not stop on failures — expand descending market cap and continue; ignore the pre-existing clock bug in `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`.

**Evidence to report:** gate status before/after; snapshot path/pages/floor/N and eligible count; if expanded: old→new N, ranks, log entry; if not: log entry + new bound; grid/aggregate/candidate output paths and any blocked/credible counts; tests after changes (or confirm unchanged if none).

---

## Turn 2026-10-25T16:25:19+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T16:25:19.444603+00:00).
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Wakeup scheduled: `wku_173e1dfe9001G3mFcVuYZMZY1M`, due `2026-10-26T15:16:00.000Z`, prompt resumes the cycle at/after the bound.
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

## Turn 2026-10-25T15:48:49+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T15:48:49.929484+00:00).
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- `git status --short` empty, `git diff --stat` empty (only handoff edits).
- Tests: 248 passed, 1 failed (pre-existing clock bug `tests/test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`).

## Turn 2026-10-25T15:48:00+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T15:47:59.168112+00:00`).
- No provider contact. `universe/last_scan.json` unchanged.
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

## Turn 2026-10-25T15:47:26+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T15:47:26.157812+00:00`).
- No provider contact. `universe/last_scan.json` unchanged.
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

## Turn 2026-10-25T15:46:48+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T15:46:48.716722+00:00`).
- No provider contact. `universe/last_scan.json` unchanged.
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

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

## Turn 2026-10-25T16:30:35+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T16:30:34.830305+00:00`).
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Tests: 248 passed, 1 failed (pre-existing clock bug `tests/test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`).
- Wakeup re-scheduled: `wku_173e6c1f4001aoV3aEMfM31ROg`, due `2026-10-26T15:16:00.000Z`, prompt resumes the cycle at/after the bound. (Previous wakeup `wku_173e1dfe9001G3mFcVuYZMZY1M` was not found in this session's pending list; re-created to guarantee the resume fires.)
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

## Turn 2026-10-25T16:36:07+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T16:36:07.794740+00:00`).
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Tests: 248 passed, 1 failed (pre-existing clock bug `tests/test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`).
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

## Turn 2026-10-25T16:42:27+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T16:42:27.093603+00:00`).
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Tests: 248 passed, 1 failed (pre-existing clock bug `tests/test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`).
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

## Turn 2026-10-25T16:50:17+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T16:50:17.646211+00:00`).
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Tests: 248 passed, 1 failed (pre-existing clock bug `tests/test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`).
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

## Turn 2026-10-25T16:53:12+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T16:53:11.915823+00:00`).
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

## Turn 2026-10-25T16:53:48+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T16:57:17.466823+00:00`).
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Wakeup scheduled: `wku_173e6c1f4001aoV3aEMfM31ROg`, due `2026-10-26T15:16:00.000Z`, prompt resumes the cycle at/after the bound.
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

## Turn 2026-10-25T16:59:31+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T16:59:37.124988+00:00`).
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Wakeup re-scheduled: `wku_17401053a001UZJPqBrPh4NcAE`, due `2026-10-26T15:16:00.000Z`, prompt resumes the cycle at/after the bound. (Previous wakeup `wku_173e6c1f4001aoV3aEMfM31ROg` was not found in this session's pending list; re-created to guarantee the resume fires.)
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

## Turn 2026-10-25T17:27:26+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T17:27:26.762861+00:00`).
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Wakeup `wku_17401053a001UZJPqBrPh4NcAE` remains scheduled due `2026-10-26T15:16:00.000Z` (resume at/after bound).
- `git status --short` empty, `git diff --stat` empty (only handoff edits).

## Turn 2026-10-25T17:30:53+00:00 (completed — offline gate check only, provider bound not yet open)
- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` 2026-10-25T17:30:53.207920+00:00`).
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Tests: 248 passed, 1 failed (pre-existing clock bug `tests/test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`).
- Wakeup scheduled: `wku_1741f054b001zQP9pW1sDn9etM`, due `2026-10-26T15:32:32.454Z`, prompt resumes the cycle at/after the bound.
- `git status --short` empty, `git diff --stat` empty (only handoff edits).
