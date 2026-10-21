#!/usr/bin/env python3
"""Same-bar SL/TP path sensitivity for the closest surviving cells.

Why this leg exists
-------------------
PROMPT.md §3.3 lists "conservative same-bar SL/TP path assumption" in the
minimum robustness set. The baseline already *is* the conservative rule: when
a bar's high and low both reach the stop and the target, the trade is closed
at the stop (`backtest.backtest.backtest_symbol`, `conservative_exit=True`).

That makes the conservative rule a floor, not a test. The test is the other
direction: if a cell only looks good because the engine happened to favour
it, then flipping the rule to the favourable path (target first) must not
change the verdict. This leg re-runs the closest surviving cells under both
rules and reports the §3.4 gate for each, so a verdict that depends on the
same-bar assumption is visible.

A cell that survives the favourable rule but not the conservative one is
fragile: its edge would be an artifact of the intrabar path assumption. A
cell that fails both is simply rejected.

Usage:
    python scripts/same_bar_sensitivity.py --run results/20261019_135940_grid \
        --audit results/20261021_005234_oos_grid_scan
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from data.data_loader import load_ohlcv_csv
from scripts.oos_grid_scan import fmt_pf, verdict
from scripts.run_grid import CONFIG_DEFAULTS, run_cell


def run_cell_leg(symbol: str, df, fast: int, slow: int, oos_fraction: float,
                 stress_multiplier: float, config: dict, conservative: bool) -> dict:
    """One cell under one same-bar rule, with the §3.4 numbers."""
    legs = {}
    for name, taker, slip in (
            ('oos', config['taker_fee_bps'], config['slippage_bps']),
            ('stress_oos', config['taker_fee_bps'] * stress_multiplier,
             config['slippage_bps'] * stress_multiplier)):
        trades, _, metrics = run_cell(
            symbol, df, fast, slow, taker, slip, config['rr'],
            config['stricter_trend'], config['min_risk_atr'], config['atr_threshold'],
            conservative, oos_fraction=oos_fraction, sizing=config['sizing'],
            risk_fraction=config['risk_fraction'],
            max_notional_multiple=config['max_notional_multiple'],
        )
        legs[name] = metrics
    full_stress_pf = None
    trades, _, full_metrics = run_cell(
        symbol, df, fast, slow, config['taker_fee_bps'] * stress_multiplier,
        config['slippage_bps'] * stress_multiplier, config['rr'],
        config['stricter_trend'], config['min_risk_atr'], config['atr_threshold'],
        conservative, oos_fraction=None, sizing=config['sizing'],
        risk_fraction=config['risk_fraction'],
        max_notional_multiple=config['max_notional_multiple'],
    )
    full_stress_pf = full_metrics.get('net_profit_factor')
    label = verdict(legs['oos'], legs['stress_oos'], full_stress_pf,
                    min_trades=30)
    return {
        'legs': legs,
        'full_sample_stress_pf': full_stress_pf,
        'decision_label': label,
    }


def main():
    parser = argparse.ArgumentParser(
        description='Same-bar SL/TP path sensitivity for the closest survivors')
    parser.add_argument('--run', type=str, required=True)
    parser.add_argument('--audit', type=str, required=True,
                        help='results/<TS>_oos_grid_scan dir; its closest survivors '
                             'are the cells that are re-run')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--oos-fraction', type=float, default=0.35)
    parser.add_argument('--stress-multiplier', type=float, default=2.0)
    parser.add_argument('--min-trades', type=int, default=30)
    parser.add_argument('--out', type=str, default=None)
    args = parser.parse_args()

    audit_dir = Path(args.audit)
    payload_audit = json.loads((audit_dir / 'summary.json').read_text())
    closest = payload_audit.get('closest_survivors') or []
    if not closest:
        raise SystemExit(f'no closest survivors in {audit_dir}/summary.json')

    config = dict(CONFIG_DEFAULTS)
    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    out_dir = Path(args.out) if args.out else Path('results') / f'{timestamp}_same_bar_sensitivity'
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for row in closest:
        symbol = row['symbol']
        fast, slow = row['P_fast'], row['P_slow']
        df = load_ohlcv_csv(str(Path(args.fixture_base) / f"{symbol.replace('/', '_')}.csv"))
        conservative = run_cell_leg(symbol, df, fast, slow, args.oos_fraction,
                                    args.stress_multiplier, config, True)
        favourable = run_cell_leg(symbol, df, fast, slow, args.oos_fraction,
                                   args.stress_multiplier, config, False)
        rows.append({
            'symbol': symbol,
            'P_fast': fast,
            'P_slow': slow,
            'in_sample_net_pf': row.get('in_sample_net_pf'),
            'in_sample_stress_net_pf': row.get('stress_net_pf'),
            'conservative': conservative,
            'favourable': favourable,
            'verdict_changes': conservative['decision_label'] != favourable['decision_label'],
        })
        print(f"{symbol} P{fast}_{slow}: conservative="
              f"{conservative['decision_label']} favourable="
              f"{favourable['decision_label']}", flush=True)

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'source_run': args.run,
        'audit': str(audit_dir),
        'oos_fraction': args.oos_fraction,
        'stress_multiplier': args.stress_multiplier,
        'config': config,
        'n_cells': len(rows),
        'n_verdict_changes': sum(1 for r in rows if r['verdict_changes']),
        'n_credible_conservative': sum(
            1 for r in rows if r['conservative']['decision_label'] == 'credible candidate'),
        'n_credible_favourable': sum(
            1 for r in rows if r['favourable']['decision_label'] == 'credible candidate'),
        'cells': rows,
    }
    payload['verdict_lines'] = [
        f"{payload['n_cells']} closest survivors were re-run under the conservative and the "
        f"favourable same-bar path assumption.",
        f"The §3.4 verdict changes for {payload['n_verdict_changes']} of them; "
        f"{payload['n_credible_conservative']} are credible under the conservative rule and "
        f"{payload['n_credible_favourable']} under the favourable one.",
    ]

    lines = ['# Same-Bar SL/TP Path Sensitivity — closest survivors\n']
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Cells:** {payload['n_cells']} (the closest survivors of `{args.audit}`)")
    lines.append(f"**Out-of-sample window:** trailing {args.oos_fraction:.0%} of each symbol's bars\n")
    lines.append('The baseline closes a same-bar stop/target conflict at the stop (adverse '
                 'first). The favourable rule closes it at the target. A verdict that only '
                 'holds under the favourable rule is an artifact of the intrabar path '
                 'assumption.\n')
    lines.append('| Symbol | Cell | OOS PF (conservative) | OOS PF (favourable) | '
                 'Stress OOS PF (conservative) | Stress OOS PF (favourable) | '
                 'Verdict (conservative) | Verdict (favourable) |')
    lines.append('|---|---|---|---|---|---|---|---|')
    for r in rows:
        c = r['conservative']['legs']
        f = r['favourable']['legs']
        lines.append(
            f"| {r['symbol']} | P{r['P_fast']}_{r['P_slow']} | "
            f"{fmt_pf(c['oos'].get('net_profit_factor'))} | "
            f"{fmt_pf(f['oos'].get('net_profit_factor'))} | "
            f"{fmt_pf(c['stress_oos'].get('net_profit_factor'))} | "
            f"{fmt_pf(f['stress_oos'].get('net_profit_factor'))} | "
            f"{r['conservative']['decision_label']} | {r['favourable']['decision_label']} |")
    lines.append('')
    lines.append('## Verdict\n')
    for line in payload['verdict_lines']:
        lines.append(f'- {line}')
    lines.append('')
    (out_dir / 'summary.md').write_text('\n'.join(lines))
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    with open(out_dir / 'config.json', 'w') as fh:
        json.dump({
            'timestamp': timestamp,
            'source_run': args.run,
            'audit': args.audit,
            'fixture_base': args.fixture_base,
            'oos_fraction': args.oos_fraction,
            'stress_multiplier': args.stress_multiplier,
            'min_trades': args.min_trades,
            'config': config,
            'command': (f'PYTHONPATH=. python3 scripts/same_bar_sensitivity.py '
                        f'--run {args.run} --audit {args.audit}'),
        }, fh, indent=2)

    print(f'\n{payload["n_cells"]} cells, {payload["n_verdict_changes"]} verdict changes, '
          f'{payload["n_credible_conservative"]} credible under the conservative rule, '
          f'{payload["n_credible_favourable"]} under the favourable one')
    print(f'Wrote {out_dir}/summary.md and summary.json')


if __name__ == '__main__':
    main()
