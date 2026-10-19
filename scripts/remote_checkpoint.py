#!/usr/bin/env python3
"""Commit and durably push the current working tree, then verify the remote SHA.

Why this exists
---------------
The workflow controller that supervises this repository checkpoints by running

    timeout --kill-after=5s 30s git push origin HEAD:$DEFAULT_BRANCH

(`.github/workflows/main.yml`, `persist_checkpoint()`), i.e. the remote write has a
**30 second budget**. `git push` must build a delta pack before it uploads
anything, and building that pack for a large new artifact set takes far longer
than 30 seconds: measured on a 4-core runner, ~450 MB of new grid artifacts
needed ~34 s just to pack and ~44 s in total, so the controller killed every
attempt and the checkpoint was reported as unpersisted.

The durable fix is to keep each checkpoint delta small. Run this script after
each finished unit of work (e.g. after every symbol of the EMA grid). Each
push then carries only that unit's delta, finishes well inside 30 seconds, and
the controller's own end-of-session push finds the remote already up to date.

Usage:
    python scripts/remote_checkpoint.py --message "chore: grid TRX"
    python scripts/remote_checkpoint.py --message "..." --branch main --timeout 900
    python scripts/remote_checkpoint.py --push-only      # no commit, just push
"""
import argparse
import fnmatch
import subprocess
import sys
from pathlib import Path

# Paths the workflow controller never stages. Mirrored here so this helper and
# the controller agree on what a checkpoint contains.
EXCLUDE_PATTERNS = [
    '.github/workflows/*',
    '.venv/*', '*/.venv/*', 'venv/*', '*/venv/*',
    'node_modules/*', '*/node_modules/*',
    '__pycache__/*', '*/__pycache__/*',
    '.pytest_cache/*', '*/.pytest_cache/*',
    '.mypy_cache/*', '*/.mypy_cache/*',
    '.ruff_cache/*', '*/.ruff_cache/*',
    '.tox/*', '*/.tox/*',
    '.env', '.env.*', '*/.env', '*/.env.*',
    '*.pyc', '*.pyo',
    '*.sqlite', '*.sqlite3', '*.db',
    '*.sqlite-wal', '*.sqlite-shm', '*.sqlite3-wal', '*.sqlite3-shm', '*.db-wal', '*.db-shm',
    '*.tmp', 'coverage.xml', '*/coverage.xml', '.coverage', '*/.coverage',
    'kilo-session-*.log', '*/kilo-session-*.log',
    'kilo-progress-*.log', '*/kilo-progress-*.log',
]


def run(cmd, timeout=None, check=True):
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if check and result.returncode != 0:
        sys.stderr.write(f'$ {" ".join(cmd)}\n{result.stdout}{result.stderr}\n')
        raise SystemExit(result.returncode)
    return result


def is_excluded(path: str) -> bool:
    return any(fnmatch.fnmatch(path, pat) for pat in EXCLUDE_PATTERNS)


def stage_changes():
    """Stage the working tree, minus the paths the controller never stages."""
    run(['git', 'add', '-A', '--', '.'])
    staged = run(['git', 'diff', '--cached', '--name-only', '-z']).stdout
    for path in staged.split('\0'):
        if path and is_excluded(path):
            run(['git', 'restore', '--staged', '--', path], check=False)
    remaining = run(['git', 'diff', '--cached', '--name-only', '-z']).stdout
    return [p for p in remaining.split('\0') if p]


def main():
    ap = argparse.ArgumentParser(description='Commit and push a durable remote checkpoint')
    ap.add_argument('--message', default='chore(kilo): checkpoint agent session')
    ap.add_argument('--branch', default='main')
    ap.add_argument('--remote', default='origin')
    ap.add_argument('--timeout', type=int, default=900,
                    help='Seconds allowed for the push (the controller only allows 30)')
    ap.add_argument('--push-only', action='store_true',
                    help='Skip staging/committing and only push the current HEAD')
    ap.add_argument('--allow-empty', action='store_true',
                    help='Commit even when there is nothing staged')
    args = ap.parse_args()

    if not args.push_only:
        staged = stage_changes()
        if staged:
            print(f'Staged {len(staged)} path(s).')
            for path in staged[:20]:
                print(f'  {path}')
            if len(staged) > 20:
                print(f'  ... and {len(staged) - 20} more')
            run(['git', 'commit', '-m', args.message])
        elif args.allow_empty:
            run(['git', 'commit', '--allow-empty', '-m', args.message])
        else:
            print('Nothing staged; pushing current HEAD only.')

    local_sha = run(['git', 'rev-parse', 'HEAD']).stdout.strip()

    fetch = run(['git', 'fetch', args.remote, args.branch], timeout=120, check=False)
    if fetch.returncode != 0:
        print('::warning::fetch failed; attempting push anyway.')
    else:
        remote_sha = run(['git', 'rev-parse', f'{args.remote}/{args.branch}']).stdout.strip()
        if remote_sha != local_sha:
            base = run(['git', 'merge-base', '--is-ancestor', remote_sha, local_sha],
                       check=False).returncode == 0
            if not base:
                print('::error::Local HEAD is not a fast-forward of the remote; refusing to push.')
                raise SystemExit(1)

    print(f'Pushing {local_sha} to {args.remote}/{args.branch} (timeout {args.timeout}s) ...')
    push = run(['git', 'push', '--progress', args.remote, f'HEAD:refs/heads/{args.branch}'],
               timeout=args.timeout, check=False)
    tail = (push.stdout + push.stderr).strip().splitlines()
    for line in tail[-8:]:
        print(line)
    if push.returncode != 0:
        print('::error::Push failed; the checkpoint is NOT durable.')
        raise SystemExit(push.returncode)

    remote_sha = run(['git', 'ls-remote', args.remote, f'refs/heads/{args.branch}']).stdout.split()
    remote_sha = remote_sha[0] if remote_sha else ''
    if remote_sha != local_sha:
        print(f'::error::Remote SHA {remote_sha} != local HEAD {local_sha}; NOT verified.')
        raise SystemExit(1)
    print(f'VERIFIED durable checkpoint at {remote_sha}.')


if __name__ == '__main__':
    main()
