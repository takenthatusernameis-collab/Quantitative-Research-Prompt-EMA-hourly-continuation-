Durable handoff (read first): NEXT_AGENT_TASK.md (append-only cycle log).

Gate: state=EXPANSION_AVAILABLE (scan 2026-11-03T01:35:03Z); next eligible refresh 2026-11-04T01:35:03.192568+00:00.

Task for next agent:
1. Offline gate check first: compare now >= next_eligible_refresh_at (2026-11-04T01:35:03.192568+00:00); verify universe/last_scan.json unchanged.
2. If not eligible: record result, append handoff entry, refresh this file, retain wakeup, no provider calls.
3. If eligible: review candidate DENT (mcap $3,269,215) for fixtures/grid coverage before any --apply; do NOT apply without coverage. No grid reruns, no candle fetches, no cost/fill changes.

Constraints unchanged.
