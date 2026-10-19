"""Universe selection and market cap ranking."""
from typing import List, Dict, Any
import json
from pathlib import Path


def load_mcap_ranking(path: str | Path) -> List[str]:
    """Load market cap ranking from JSON file."""
    path = Path(path)
    with path.open('r') as f:
        data = json.load(f)
    if isinstance(data, dict) and 'symbols' in data:
        return list(data['symbols'])
    if isinstance(data, list):
        return list(data)
    raise ValueError("Invalid mcap ranking format")


def load_mcap_snapshot(path: str | Path) -> Dict[str, Any]:
    """Load the full market-cap ranking snapshot, including provenance metadata.

    Returns a dict with at least a 'symbols' list plus any snapshot metadata
    (snapshot_id, snapshot_source, updated_at, added_in_this_expansion, ...).
    """
    path = Path(path)
    with path.open('r') as f:
        data = json.load(f)
    if isinstance(data, list):
        data = {'symbols': list(data)}
    if not isinstance(data, dict):
        raise ValueError("Invalid mcap ranking format")
    data.setdefault('symbols', [])
    return data


def save_mcap_ranking(symbols: List[str], path: str | Path, updated_at: str | None = None):
    """Save market cap ranking to JSON file."""
    import datetime
    if updated_at is None:
        updated_at = datetime.datetime.utcnow().isoformat() + 'Z'
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        'updated_at': updated_at,
        'symbols': symbols
    }
    with path.open('w') as f:
        json.dump(data, f, indent=2)
    return data
