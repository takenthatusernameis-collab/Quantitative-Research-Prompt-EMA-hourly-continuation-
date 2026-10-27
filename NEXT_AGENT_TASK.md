# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-27T23:02Z)

- Gate re-checked offline this turn: eligible=False; bound 2026-10-28T19:29:54.929656+00:00 not yet elapsed (~20.5 h remaining). Command: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`. No provider contact this turn. Wakeup already set at/after the bound — do not re-schedule a duplicate.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES; snapshot mcap_snapshot_20261027_192954 (CoinGecko, 20/20 pages, 2000 entries, lowest rank 2000 at $3 373 017); coverage reaches below the expansion floor.
- Universe N = 275; expansion floor ALPINE/USDT $3 489 697; eligible_unseen_below_floor_count = 0; batch_selected = []; no universe expansion.
- Baseline grid results/20261019_135940_grid re-verified directly: all_symbols_processed=true, completed_cells=18150 (275 x 66), 0 blocked; pooled mean net PF 0.4987, 37 cells net PF > 1, 27 exploratory, 18123 rejected, **0 credible candidates**.
- Child mutation grids C_min_risk_atr (results/20261022_134500_grid) and C_stricter_trend (results/20261022_134500_grid) both complete, NOT_PROMOTED; baseline grid remains the program grid (results/mutations.json).
- git status --short empty; git diff --stat empty; pytest tests/ -q -> 248 passed, 1 failed (pre-existing clock bug test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible, left untouched per AGENTS.md #6).
- Wakeup re-set this turn (prior id stale/cross-session): due 2026-10-28T19:35:00Z (at/after bound 2026-10-28T19:29:54.929656+00:00), id **wku_17f9a27aa0014lNoHSZZ0NhVbN**. Only one pending wakeup exists for this session; do not re-schedule a duplicate.

## Next action at/after bound

At/after 2026-10-28T19:29:54.929656+00:00:
1. Check gate offline (PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"). If not yet eligible, re-set a wakeup at/after the bound and stop — no provider contact.
2. If eligible: run exactly one 20-page CoinGecko ranking pass (PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20).
3. Recompute the expansion floor from the fresh snapshot; inspect the band strictly below the floor.
4. If eligible_unseen_below_floor_count == 0: record the pass in universe/last_scan.json (state AWAITING_NEW_ELIGIBLE_CANDIDATES, batch_selected = []) and set a +24 h bound (next_eligible_refresh_at = scanned_at + 24 h).
5. Else (eligible names exist): expand per PROMPT.md §2.1 (append next lower market-cap names, update universe/mcap_rank.json + mcap_expansion_log.md, then run the full 66-pair grid on each new symbol).
6. Update both handoffs (NEXT_AGENT_TASK.md and INITIAL_TASK_FOR_NEXT_AGENT.md) with the result.

## Constraints

- No provider before bound; historical research only.
- One 20-page pass per cycle maximum; do not poll CoinGecko while waiting.
- Do not trigger, cancel, rerun, or dispatch GitHub Actions; do not edit workflow files.
- Do not fetch new candle data; do not modify the baseline grid or registered costs/fills/entry-exit semantics.
- Preserve all negative and blocked results; never label a partial grid complete.
- A negative result is a valid research result; expand rather than stop.

(End of file - total 30 lines)