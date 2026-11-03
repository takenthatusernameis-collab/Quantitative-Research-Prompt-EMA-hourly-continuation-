# Initial task for next agent

Durable handoff: `NEXT_AGENT_TASK.md` (append-only cycle log). Read it first.

## Gate state (as of 2026-11-03T04:30:59Z)

- Gate: **NOT ELIGIBLE**. `universe/last_scan.json` `next_eligible_refresh_at` = `2026-11-04T01:35:03.192568+00:00`. Now is before that bound (~21h04m remaining).
- State: `EXPANSION_AVAILABLE`. Snapshot `universe/mcap_snapshot_20261103_013503.json` (scanned_at `2026-11-03T01:35:03.192568+00:00`, 20/20 pages, 2000 entries, lowest mcap $3,225,884).
- Universe: N=275. Expansion floor `ALPINE/USDT` $3,392,434 (rank 1970).
- Below-floor band (mcap < $3,392,434): 30 entries; 29 excluded — 28 by `no_tradable_kucoin_spot_usdt_pair`, 1 by `insufficient_hourly_history_for_grid` (HPP rank 1975). Exactly 1 eligible unseen: **`DENT/USDT`** rank 1989, mcap $3,269,215, `kucoin_usdt_pair=true`, `exclusion_reason=null`. `eligible_unseen_below_floor_count=1`, `batch_selected=["DENT/USDT"]`.

## Task for next agent

1. **Offline gate check first**: compare now >= `next_eligible_refresh_at` (`2026-11-04T01:35:03.192568+00:00`); verify `universe/last_scan.json` unchanged (snapshot_id `mcap_snapshot_20261103_013503`, state `EXPANSION_AVAILABLE`, eligible_unseen_below_floor_count=1, batch_selected=["DENT/USDT"]).
2. **If not eligible** (still before the bound): record result, append a handoff entry to `NEXT_AGENT_TASK.md`, refresh this file, retain wakeup `wku_19fae6e7b001taqzJsjpRjuRpU` due `2026-11-04T01:40:00.000Z`, make NO provider calls.
3. **If eligible**: review candidate `DENT/USDT` (rank 1989, mcap $3,269,215) for fixtures/grid coverage before any `--apply`; do NOT apply without coverage. Check `data/fixtures/DENT_USDT.csv` and existing grid configs. If a fresh snapshot pass is warranted, run at most one 20-page pass: `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`, recompute the floor, inspect the below-floor band, and update `universe/last_scan.json`. No grid reruns, no candle fetches, no cost/fill changes unless explicitly justified and versioned per AGENTS.md.

## Constraints (unchanged)

- Historical research only. Never place orders or deploy live/paper trading. Use only free public data and no-cost tooling.
- Preserve the documented EMA signal, fill logic and cost assumptions unless a new, versioned experiment explicitly changes them. Never describe fixtures as market evidence.
- Keep a strict confirmatory run separate from exploratory pilots. Do not silently reduce frozen history, sample, execution or cost requirements; a relaxed version must get a new ID and report survivorship, selection, uncertainty and cost sensitivity.
- Preserve all negative and blocked results. Do not select a winner on the final holdout or claim profitability without auditable net-of-cost results, data provenance and independent checks.
- After three materially distinct attempts across two independent data/source approaches fail the same feasibility gate — or when a documented structural limit makes the gate unattainable — stop repeating the same failure and complete the next bounded, no-cost exploratory or source-independent task.
- Never modify unrelated projects or trigger paid services. Inspect diffs and retain a clear research handoff with exact evidence and one measurable next task.

## Resume wakeup

`wku_19fae6e7b001taqzJsjpRjuRpU` due `2026-11-04T01:40:00.000Z` (just after the gate bound; do not duplicate).