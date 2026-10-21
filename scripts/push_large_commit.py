#!/usr/bin/env python3
"""Push a large commit in chunks the remote accepts.

Why this exists
---------------
The controller's checkpoint persistence gives `git push` a 30 s window. A
checkpoint that adds the full grid artifacts carries ~2.1 GiB of new objects,
and a single push of that size does not finish inside the window - and on
this repository it does not finish at all:

    Writing objects: 100% (105658/105658), 2.11 GiB | 28.28 MiB/s, done.
    error: RPC failed; HTTP 500 curl 22 The requested URL returned error: 500
    send-pack: unexpected disconnect while reading sideband packet
    fatal: the remote end hung up unexpectedly

The remote closes the connection while the pack is still being written, and
the ref update never happens. The failure is a *size* failure, not a
permission, network or authentication failure: a dry-run push of the same
ref negotiates fine, a tiny probe branch can be created and deleted with the
same credentials, and the objects themselves are accepted - it is the single
2.1 GiB transfer that the server refuses.

What this script does
---------------------
It splits the transfer into several smaller pushes and then pushes the real
commit, unchanged, on top of it:

1. The new blobs of the commit are grouped into batches of a bounded size.
2. Each batch is materialised as a throwaway commit on a temporary branch
   (the base tree plus that batch's files) and pushed. The remote accepts
   each small push and keeps the objects.
3. The batch commits are chained, so the last one is an ancestor of nothing
   but reaches every batch's blobs. The remote therefore already has every
   object of the real commit.
4. The real commit is then pushed to the target branch. Only the tree and
   commit objects are still missing, so the final push is small and finishes
   in seconds.

The target branch's history is not rewritten: the real commit is pushed as
it is, the batch commits live on a temporary branch that is deleted
afterwards, and the local repository is left untouched.

Usage:
    python scripts/push_large_commit.py --head HEAD --branch main
"""
import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path


def run(args, **kwargs):
    return subprocess.run(args, check=True, capture_output=True, text=True, **kwargs)


def git_out(args, **kwargs):
    return subprocess.check_output(args, text=True, **kwargs)


def changed_blobs(base: str, head: str) -> list:
    """(mode, blob, path) of every file the commit range adds or changes."""
    raw = subprocess.check_output(
        ['git', 'diff-tree', '-r', '--raw', '--no-renames', '-z', base, head])
    fields = raw.split(b'\0')
    entries = []
    # With -z the record is "<header>\0<path>\0": the header carries the two
    # modes, the two object names and the status, the path is its own field.
    for i in range(0, len(fields) - 1, 2):
        header = fields[i]
        path = fields[i + 1]
        if not header.startswith(b':') or not path:
            continue
        parts = header.split()
        if len(parts) < 5:
            continue
        # ":<old mode> <new mode> <old sha> <new sha> <status>"
        mode = parts[0].decode().lstrip(':')
        new_sha = parts[3].decode()
        if not new_sha or set(new_sha) == {'0'}:
            continue
        entries.append((mode, new_sha, path.decode('utf-8', 'surrogateescape')))
    return entries


def object_sizes(shas: list) -> dict:
    if not shas:
        return {}
    payload = '\n'.join(shas) + '\n'
    proc = subprocess.run(['git', 'cat-file', '--batch-check'],
                          input=payload, capture_output=True, text=True)
    sizes = {}
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 3 and parts[1] == 'blob':
            sizes[parts[0]] = int(parts[2])
    return sizes


def main():
    parser = argparse.ArgumentParser(description='Chunked push of a large commit')
    parser.add_argument('--head', type=str, default='HEAD')
    parser.add_argument('--branch', type=str, default='main')
    parser.add_argument('--remote', type=str, default='origin')
    parser.add_argument('--batch-bytes', type=int, default=180 * 1024 * 1024)
    parser.add_argument('--base', type=str, default=None,
                        help='base commit of the range (default: the remote branch)')
    parser.add_argument('--temp-branch', type=str, default=None)
    parser.add_argument('--keep-temp-branch', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    head = git_out(['git', 'rev-parse', args.head]).strip()
    if args.base:
        base = git_out(['git', 'rev-parse', args.base]).strip()
    else:
        base = git_out(['git', 'rev-parse', f'{args.remote}/{args.branch}']).strip()
    temp_branch = args.temp_branch or f'kilo-batch-push-{head[:10]}'

    if not git_out(['git', 'merge-base', '--is-ancestor', base, head]).strip():
        pass
    print(f'base {base} -> head {head}', flush=True)

    entries = changed_blobs(base, head)
    sizes = object_sizes([sha for _, sha, _ in entries])
    total = sum(sizes.get(sha, 0) for _, sha, _ in entries)
    print(f'{len(entries)} changed files, {total / 1073741824:.2f} GiB of new blobs',
          flush=True)

    batches = []
    current = []
    current_bytes = 0
    for mode, sha, path in entries:
        size = sizes.get(sha, 0)
        if current and current_bytes + size > args.batch_bytes:
            batches.append(current)
            current = []
            current_bytes = 0
        current.append((mode, sha, path))
        current_bytes += size
    if current:
        batches.append(current)

    print(f'{len(batches)} batches of at most {args.batch_bytes / 1048576:.0f} MiB',
          flush=True)
    if args.dry_run:
        for i, batch in enumerate(batches, 1):
            size = sum(sizes.get(sha, 0) for _, sha, _ in batch)
            print(f'  batch {i}: {len(batch)} files, {size / 1048576:.1f} MiB')
        return 0

    index_path = Path(tempfile.gettempdir()) / f'kilo-batch-index-{head[:10]}'
    env = dict(os.environ, GIT_INDEX_FILE=str(index_path))
    parent = base
    for i, batch in enumerate(batches, 1):
        if index_path.exists():
            index_path.unlink()
        run(['git', 'read-tree', base], env=env)
        # One index-info call per batch: the per-file update-index calls cost
        # one process each, which is minutes over a whole grid.
        index_info = ''.join(f'{mode} {sha}\t{path}\n' for mode, sha, path in batch)
        run(['git', 'update-index', '--index-info'], env=env, input=index_info)
        tree = git_out(['git', 'write-tree'], env=env).strip()
        commit = git_out(['git', 'commit-tree', tree, '-p', parent,
                          '-m', f'kilo batch {i}/{len(batches)} (transfer scaffold)'],
                         env=env).strip()
        run(['git', 'push', '--quiet', args.remote, f'{commit}:refs/heads/{temp_branch}'])
        parent = commit
        size = sum(sizes.get(sha, 0) for _, sha, _ in batch)
        print(f'  batch {i}/{len(batches)}: {len(batch)} files, '
              f'{size / 1048576:.1f} MiB pushed', flush=True)
    if index_path.exists():
        index_path.unlink()

    # The real commit, unchanged, on the target branch.
    run(['git', 'push', args.remote, f'{head}:refs/heads/{args.branch}'])
    remote = git_out(['git', 'ls-remote', args.remote, f'refs/heads/{args.branch}']).split()
    print(f'remote {args.branch} is now {remote[0]}')
    if not args.keep_temp_branch:
        run(['git', 'push', '--quiet', args.remote, f':refs/heads/{temp_branch}'])
        print(f'deleted the temporary branch {temp_branch}')
    if remote[0] != head:
        print('ERROR: the remote branch does not hold the pushed commit',
              file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
