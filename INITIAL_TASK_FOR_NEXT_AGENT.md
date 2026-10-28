# Initial Task For Next Agent

Read this handoff first: `NEXT_AGENT_TASK.md` (durable state + exact next action).

## Situation at wakeup (re-checked 2026-10-28T11:30:15Z)

Gate is NOT eligible: bound `2026-10-28T19:29:54.929656+00:00` has not yet elapsed.
Last pass: `mcap_snapshot_20261027_192954` (CoinGecko, 20/20 pages, 2000 entries).
Gate re-checked offline at 2026-10-28T11:25:57.161055+00:00 → `eligible=False` (reason: the 24 h refresh bound `2026-10-28T19:29:54.929656+00:00` has not elapsed yet). No provider contact permitted before bound. Step 1 complete — STOP.
Wakeup: `wku_18249656f001GoH2ry4xaolvaF` due `2026-10-28T19:40:00.000Z` (~after bound), set this turn. Re-set at/after bound if this wakeup is cleared before eligibility.

## Exact steps (do this in order)

1. **Check gate offline**
   `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`
   - If `eligible=False`: re-set a wakeup at/after the bound and **STOP** — no provider contact. Update both handoffs with the new wakeup id/time.
   - If `eligible=True`: proceed to step 2.

2. **Run exactly one 20-page CoinGecko ranking pass** (one pass max per cycle)
   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`

3. **Recompute floor from fresh snapshot; inspect band strictly below floor**
   Check `eligible_unseen_below_floor_count` against fresh snapshot.

4. **If `eligible_unseen_below_floor_count == 0`**
   Record the pass in `universe/last_scan.json` (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `batch_selected = []`), set `next_eligible_refresh_at = scanned_at + 24h`, re-set wakeup at/after that bound, and **STOP**.

5. **If `eligible_unseen_below_floor_count > 0`**
   Expand per PROMPT.md §2.1 (append next lower market-cap names, update `universe/mcap_rank.json` + `universe/mcap_expansion_log.md`), then run the full 66-pair grid on each new symbol.
   Update both handoffs with results (snapshot, floor, eligible count, batch, next bound/wakeup).

## Hard constraints

- No provider before bound; historical research only. Never describe fixtures as market evidence.
- Do not trigger/cancel/rerun/dispatch GitHub Actions; do not edit workflow files.
- Do not fetch new candle data; do not modify baseline grid or registered costs/fills/entry-exit semantics.
- Preserve all negative/blocked results; never label a partial grid complete.
- A negative result is valid — expand rather than stop.

## Static context

- Universe N=275; expansion floor ALPINE/USDT $3,489,697; eligible_unseen_below_floor_count=0; batch_selected=[] (no expansion this turn).
- Baseline grid `results/20261019_135940_grid`: 18150 cells, pooled mean net PF 0.4987, 0 credible candidates.
- Mutations C_min_risk_atr, C_stricter_trend: complete, NOT_PROMOTED; baseline remains program grid.
- Tests: 248 passed, 1 failed (pre-existing clock bug `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`, untouched per AGENTS.md #6).