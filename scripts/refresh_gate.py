#!/usr/bin/env python3
"""The 24 h refresh bound of the market-cap ranking (PROMPT.md §2.1.5).

PROMPT.md §2.1.5 asks for the market-cap ranking to be refreshed at least once
every 24 h while the program waits for new candidates, and explicitly forbids
querying the provider on every agent activation. The bound therefore has to
live in the scan record and in code - not in the memory of an agent - because
every pass re-queries the provider and moves the expansion floor.

Two tools can query the provider: `scripts/refresh_universe.py` (the gated
entry point) and `scripts/fetch_mcap_snapshot.py` (the classic path, kept as a
fallback). Both refuse a pass before the bound has elapsed, and both write the
bound of the pass they made into `universe/last_scan.json`. The logic lives
here so that the two tools cannot drift apart.
"""
from datetime import datetime, timedelta, timezone

# PROMPT.md §2.1.5: refresh the ranking at least once every 24 h, and not on
# every agent activation.
REFRESH_INTERVAL_HOURS = 24


def parse_iso(value):
    """Parse an ISO-8601 timestamp into an aware UTC datetime."""
    if value is None:
        return None
    text = str(value).strip()
    if text.endswith('Z'):
        text = text[:-1] + '+00:00'
    stamp = datetime.fromisoformat(text)
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    return stamp.astimezone(timezone.utc)


def iso(stamp) -> str:
    """An aware UTC datetime as an ISO-8601 string."""
    return stamp.astimezone(timezone.utc).isoformat()


def bound_after(scanned_at, hours: int = REFRESH_INTERVAL_HOURS) -> str:
    """The next eligible refresh: the time of the ranking pass plus 24 h.

    `scanned_at` is the timestamp of the pass (ISO-8601). The bound belongs to
    the *ranking pass*, not to the moment a batch is applied: applying a frozen
    snapshot again does not refresh the ranking and must not move the bound.
    """
    stamp = parse_iso(scanned_at) or datetime.now(timezone.utc)
    return iso(stamp + timedelta(hours=hours))


def gate_status(state: dict, now=None) -> dict:
    """Is a market-cap refresh allowed at `now`?

    `next_eligible_refresh_at` is the bound of PROMPT.md §2.1.5: 24 h after
    the last pass, while the program waits for new candidates. A record
    without a bound means the ranking band was not exhausted at the last pass,
    so the next pass may run at any time - the frozen snapshot of that pass is
    what the expansion works on.
    """
    now = now or datetime.now(timezone.utc)
    bound = state.get('next_eligible_refresh_at')
    if not bound:
        return {'eligible': True, 'bound': None, 'now': iso(now),
                'reason': 'no refresh bound recorded (the ranking band was not exhausted)'}
    due = parse_iso(bound)
    if now >= due:
        return {'eligible': True, 'bound': bound, 'now': iso(now),
                'reason': f'the 24 h refresh bound {bound} has elapsed'}
    return {'eligible': False, 'bound': bound, 'now': iso(now),
            'reason': f'the 24 h refresh bound {bound} has not elapsed yet'}


def require_open_gate(state: dict, now=None, override_reason=None) -> dict:
    """Raise SystemExit unless a refresh is allowed right now.

    An override needs a written reason: it is the documented way to run one
    extra pass (for example after a pass that came back incomplete), never a
    way to poll the provider.
    """
    gate = gate_status(state, now)
    if gate['eligible']:
        return gate
    if not override_reason:
        raise SystemExit(
            f'refresh refused: {gate["reason"]}. The ranking must not be queried '
            f'more than once per 24 h (PROMPT.md §2.1.5). Use --override-gate '
            f'--override-reason "<reason>" to override this deliberately.')
    return gate


def override_reason(args) -> str:
    """The documented reason for overriding the 24 h bound, or None.

    Both flags are needed: `--override-gate` alone is a typo, and a reason
    without the flag is not a deliberate override. The gate is the only thing
    that keeps the provider from being queried on every agent activation, so
    an override has to be an explicit, written decision.
    """
    if not getattr(args, 'override_gate', False):
        return None
    return getattr(args, 'override_reason', None)
