# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-28T09:24:17Z)

- Gate re-checked offline this turn (2026-10-28T09:34:15.684191+00:00): `eligible=False` (bound `2026-10-28T19:29:54.929656+00:00` not elapsed). No provider contact. Step 1 complete — STOP.
- Wakeup `wku_181daec18001InGwEZBFx49Q7k` due 2026-10-28T19:35:00Z (~after bound 19:29:54.929656+00:00), set this turn (gate re-checked offline 2026-10-28T09:34:15.684191+00:00 → eligible=False; no provider contact).
- Last scan: `mcap_snapshot_20261027_192954` (CoinGecko, 20/20 pages, 2000 entries, lowest rank 2000 at $3,373,017). Coverage reaches below expansion floor.
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`; snapshot `mcap_snapshot_20261027_192954`; eligible_unseen_below_floor_count=0; batch_selected=[]; no universe expansion.
- Universe N=275; expansion floor ALPINE/USDT $3,489,697.
- Baseline grid `results/20261019_135940_grid`: all_symbols_processed=true, completed_cells=18150 (275×66), 0 blocked; pooled mean net PF 0.4987, 37 cells net PF>1, 27 exploratory, 18123 rejected, **0 credible candidates**.
- Child mutation grids `results/20261022_134500_grid` (C_min_risk_atr) and (C_stricter_trend): both complete, NOT_PROMOTED; baseline remains program grid (`results/mutations.json`).
- git status --short empty; git diff --stat empty. `pytest tests/ -q` → 248 passed, 1 failed (pre-existing clock bug `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`, left untouched per AGENTS.md #6).

## Next action at/after bound

At/after `2026-10-28T19:29:54.929656+00:00`:

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