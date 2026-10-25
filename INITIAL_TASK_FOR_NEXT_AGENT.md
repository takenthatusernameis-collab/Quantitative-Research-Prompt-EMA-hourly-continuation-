# Initial Task For Next Agent — Durable Handoff

**Re-verified at:** 2026-10-25T15:46:48+00:00
**Repo:** Quantitative-Research-Prompt-EMA-hourly-continuation-
**Status:** AWAITING_NEW_ELIGIBLE_CANDIDATES (Batch 30 done 2026-10-25T15:14:53Z)

## State summary
- Last scan: `universe/mcap_snapshot_20261025_151453.json` (2026-10-25T15:14:53.192289Z)
- Coverage: 2000 entries, rank 2000 ~ $3,338,115; coverage_reaches_below_floor = true
- Universe: N=275 (BTC/USDT ... ALPINE/USDT), floor ALPINE/USDT $3,405,003
- Eligible unseen below floor: 0
- Next refresh bound: `2026-10-26T15:14:53.192289+00:00`
- Baseline grid: `results/20261019_135940_grid` — 275x66, all processed, 0 blocked, 0 credible candidates
- Tests: 248 passed, 1 failed (pre-existing `test_refresh_gate.py` clock bug)

## Exact task to run
Wait for gate to open (after `2026-10-26T15:14:53.192289+00:00`). Then:

1. Check gate: `PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"` → must be `eligible: True`. If False, stop and report bound.
2. Run exactly one 20-page pass: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20` (only provider contact this cycle).
3. Check `eligible_unseen_below_floor_count`.
4. If candidates: expand universe, fetch OHLCV via `scripts/fetch_kucoin.py`, run grid with `--mcap universe/mcap_rank.json --n <NEW_N> --fixture-base data/fixtures --resume results/20261019_135940_grid`. Then aggregate/candidate check on the same grid. Do **not** create a second grid writer.
5. If none: log pass to `universe/mcap_expansion_log.md`, set state to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, set next bound to +24h from new scan time.
6. Update `NEXT_AGENT_TASK.md` and this file.

## Hard constraints
- No provider call before bound.
- No second writer on baseline grid; no partial-grid promotion.
- No changes to costs/folds/entry-exit/gates.
- Do not combine variables.
- Do not stop on failures; expand down market cap per PROMPT.
- Ignore pre-existing clock bug in `test_refresh_gate.py`.

## Evidence to report
- Gate status before/after
- Snapshot path/pages/floor/N and eligible count
- If expanded: old->new N, ranks, log entry
- If not: log entry + new bound
- Grid/aggregate/candidate outputs paths and any blocked/credible counts
- Tests after changes (or confirm unchanged if none)
