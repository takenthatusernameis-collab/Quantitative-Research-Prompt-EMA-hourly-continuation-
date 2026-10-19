#!/usr/bin/env python3
"""Cost stress test harness: compares baseline vs 2x fees/slippage.

Runs the EMA hourly continuation backtest at the configured cost and at 2x
cost, then reports how net metrics (profit factor, win rate, Sharpe) degrade.
"""
import argparse
import json
from pathlib import Path
from datetime import datetime

import pandas as pd

from data.data_loader import load_ohlcv_csv
from signals.signals import generate_signals
from universe.universe import load_mcap_ranking, save_mcap_ranking
from backtest.backtest import backtest_symbol
from metrics.metrics import calculate_metrics


def run(symbols, taker_fee_bps, slippage_bps, n, rr=1.0, stricter_trend=False, min_risk_atr=False, atr_threshold=1.0):
    """Run backtest over symbols and return pooled trades + equity + metrics."""
    from pathlib import Path
    fixture_base = Path('data') / 'fixtures'
    all_trades = []
    all_equity = []
    for symbol in symbols[:n]:
        sym_file = fixture_base / f'{symbol.replace("/", "_")}.csv'
        df = load_ohlcv_csv(sym_file) if sym_file.exists() else load_ohlcv_csv(Path('data') / 'fixtures' / 'sample_hourly.csv')
        df_sig = generate_signals(df.copy(), stricter_trend=stricter_trend)
        trades, equity_df = backtest_symbol(
            df_sig, symbol=symbol,
            taker_fee_bps=taker_fee_bps, slippage_bps=slippage_bps, rr=rr, min_risk_atr=min_risk_atr, atr_threshold=atr_threshold,
        )
        all_trades.extend(trades)
        all_equity.append(equity_df)

    if all_equity:
        equity_result = all_equity[0].copy()
        import numpy as np
        equity_vals = np.mean([eq['equity'].values for eq in all_equity], axis=0)
        equity_result['equity'] = equity_vals
    else:
        equity_result = pd.DataFrame(columns=['timestamp', 'equity'])

    metrics = calculate_metrics(all_trades, equity_result, symbol='pooled')
    return all_trades, equity_result, metrics


def main():
    parser = argparse.ArgumentParser(description='Cost stress test (1x vs 2x fees/slippage)')
    parser.add_argument('--fixture', type=str, required=False)
    parser.add_argument('--mcap', type=str, required=False)
    parser.add_argument('--n', type=int, default=3)
    parser.add_argument('--taker-fee-bps', type=float, default=10.0)
    parser.add_argument('--slippage-bps', type=float, default=2.0)
    parser.add_argument('--stress-multiplier', type=float, default=2.0,
                        help='Multiplier applied to fees/slippage for stress leg')
    parser.add_argument('--rr', type=float, default=1.0)
    parser.add_argument('--stricter-trend', action='store_true')
    parser.add_argument('--min-risk-atr', action='store_true')
    parser.add_argument('--atr-threshold', type=float, default=1.0)
    args = parser.parse_args()

    # Create results directory
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    results_dir = Path('results') / f'{timestamp}_cost_stress'
    results_dir.mkdir(parents=True, exist_ok=True)

    # Load universe
    if args.mcap:
        symbols = load_mcap_ranking(args.mcap)
    else:
        default_mcap = Path('universe') / 'mcap_rank.json'
        if not default_mcap.exists():
            save_mcap_ranking(['BTC/USDT', 'ETH/USDT', 'SOL/USDT'], default_mcap)
        symbols = load_mcap_ranking(default_mcap)

# Data loaded per-symbol in run()
    df = None

    # Baseline leg (1x cost)
    _, _, base_metrics = run(
        symbols, args.taker_fee_bps, args.slippage_bps, args.n, rr=args.rr,
        stricter_trend=args.stricter_trend, min_risk_atr=args.min_risk_atr, atr_threshold=args.atr_threshold,
    )
    # Stress leg (multiplier x cost)
    stress_taker = args.taker_fee_bps * args.stress_multiplier
    stress_slippage = args.slippage_bps * args.stress_multiplier
    _, _, stress_metrics = run(
        symbols, stress_taker, stress_slippage, args.n, rr=args.rr,
        stricter_trend=args.stricter_trend, min_risk_atr=args.min_risk_atr, atr_threshold=args.atr_threshold,
    )

    comparison = {
        'base_taker_fee_bps': args.taker_fee_bps,
        'base_slippage_bps': args.slippage_bps,
        'stress_taker_fee_bps': stress_taker,
        'stress_slippage_bps': stress_slippage,
        'stress_multiplier': args.stress_multiplier,
        'base': {k: base_metrics.get(k) for k in [
            'trade_count', 'net_profit_factor', 'net_win_rate',
            'sharpe_ratio', 'sortino_ratio', 'max_drawdown', 'cagr',
            'net_avg_win', 'net_avg_loss', 'exposure', 'avg_hold_time_bars',
        ]},
        'stress': {k: stress_metrics.get(k) for k in [
            'trade_count', 'net_profit_factor', 'net_win_rate',
            'sharpe_ratio', 'sortino_ratio', 'max_drawdown', 'cagr',
            'net_avg_win', 'net_avg_loss', 'exposure', 'avg_hold_time_bars',
        ]},
    }

    # Delta: stress - base
    keys = ['net_profit_factor', 'net_win_rate', 'sharpe_ratio', 'sortino_ratio',
            'max_drawdown', 'cagr', 'net_avg_win', 'net_avg_loss']
    comparison['delta'] = {
        k: (comparison['stress'].get(k) or 0) - (comparison['base'].get(k) or 0)
        for k in keys
    }

    with open(results_dir / 'cost_stress.json', 'w') as f:
        json.dump(comparison, f, indent=2, default=str)

    # Markdown summary
    with open(results_dir / 'summary.md', 'w') as f:
        f.write('# Cost Stress Test (1x vs {:.0f}x fees/slippage)\n\n'.format(args.stress_multiplier))
        f.write(f'**Timestamp:** {timestamp}\n\n')
        f.write('| Metric | Base | Stress | Delta |\n|---|---|---|---|\n')
        for k in keys:
            b = comparison['base'].get(k)
            s = comparison['stress'].get(k)
            d = comparison['delta'].get(k)
            def fmt(v):
                if v is None:
                    return 'n/a'
                if isinstance(v, float) and (v == float('inf') or v == float('-inf')):
                    return 'inf' if v > 0 else '-inf'
                return f'{v:.4f}'
            f.write(f'| {k} | {fmt(b)} | {fmt(s)} | {fmt(d)} |\n')
        f.write(f'\nTrade count: base={comparison["base"].get("trade_count")}, '
                f'stress={comparison["stress"].get("trade_count")}\n')

    print(f'Cost stress results saved to {results_dir}')
    print(f'Base net PF: {comparison["base"].get("net_profit_factor")} -> '
          f'Stress net PF: {comparison["stress"].get("net_profit_factor")}')


if __name__ == '__main__':
    main()
