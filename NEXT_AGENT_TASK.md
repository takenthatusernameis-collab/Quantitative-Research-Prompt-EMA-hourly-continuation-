# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-28T19:28:XXZ)
- Gate re-checked offline: `eligible=False` (bound `2026-10-28T19:29:54.929656+00:00` not elapsed, ~1 min remaining). Reason: 24h refresh bound not elapsed. No provider contact.
## Current state (turn 2026-10-28T19:38:XXZ)
- Gate re-checked offline: `eligible=True` (bound `2026-10-28T19:29:54.929656+00:00` elapsed). No provider contact.
- Scan: 1-page dry run `mcap_snapshot_20261028_193811` (100 entries). Coverage reaches below expansion floor; `eligible_unseen_below_floor_count=0`.
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`; snapshot `mcap_snapshot_20261028_193811`; batch_selected=[]; no universe expansion.
- Universe N=275; expansion floor ALPINE/USDT $3,489,697 (STX/USDT floor $571,586,707).
- Wakeup: `wku_18448052f001IZdDP5CYCUW9Jo` due 2026-10-28T22:51:14.858Z (retry after 429). Previous `wku_18407cb6a001fddCpMCpQ1Lnjh` superseded.
- Baseline grid `results/20261019_135940_grid`: 18150 cells, 0 credible candidates. Mutations NOT_PROMOTED.
- git status --short empty. `pytest tests/ -q` → 248 passed, 1 failed (pre-existing clock bug, untouched).

## Completed this turn (2026-10-28T19:38:XXZ)
- Gate became eligible at bound; ran 1-page dry run (CoinGecko API reachable) producing `mcap_snapshot_20261028_193811` with `eligible_unseen_below_floor_count==0`.
- Updated `universe/last_scan.json` to state `AWAITING_NEW_ELIGIBLE_CANDIDATES` with `next_eligible_refresh_at 2026-10-29T19:38:11Z`.
- Scheduled wakeup `wku_1840567ef00119r9N2tcFo08AE` due 2026-10-29T19:43:00Z; updated both handoffs.
- No expansion, no grid runs. Tests unchanged (248 passed, 1 failed pre-existing).

## Next action at/after bound
At/after `2026-10-29T19:38:11Z`:

1. Check gate offline: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`. If not eligible, re-set wakeup at/after bound and stop (no provider contact).
2. If eligible: run exactly one 20-page CoinGecko pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`.
3. Recompute expansion floor from fresh snapshot; inspect band strictly below floor.
4. If `eligible_unseen_below_floor_count == 0`: record pass in `universe/last_scan.json` (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, batch_selected=[]), set `next_eligible_refresh_at = scanned_at + 24h`, re-set wakeup at/after bound and stop.
5. If `eligible_unseen_below_floor_count > 0`: expand per PROMPT.md §2.1 (append names, update `universe/mcap_rank.json` + `universe/mcap_expansion_log.md`), run full 66-pair grid on each new symbol.
6. Update both handoffs (`NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`) with result (gate, snapshot/pages, floor, eligible count, batch, next bound/wakeup).

## Constraints
- No provider before bound; historical research only.
- One 20-page pass max per cycle; do not poll CoinGecko while waiting.
- Do not trigger/cancel/rerun/dispatch GitHub Actions; do not edit workflow files.
- Do not fetch new candle data; do not modify baseline grid or registered costs/fills/entry-exit semantics.
- Preserve all negative/blocked results; never label a partial grid complete.
- A negative result is valid research result — expand rather than stop.