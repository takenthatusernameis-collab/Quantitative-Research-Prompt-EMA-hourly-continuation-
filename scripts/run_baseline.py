#!/usr/bin/env python3
"""Run baseline backtest."""
import argparse
import json
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np

from data.data_loader import load_ohlcv_csv
from signals.signals import generate_signals
from universe.universe import load_mcap_ranking, save_mcap_ranking
from backtest.backtest import backtest_symbol
from metrics.metrics import calculate_metrics


def main():
    parser = argparse.ArgumentParser(description='Run EMA hourly continuation baseline')
    parser.add_argument('--fixture', type=str, help='Path to CSV fixture')
    parser.add_argument('--mcap', type=str, help='Path to mcap ranking JSON')
    parser.add_argument('--n', type=int, default=3, help='Number of symbols to process')
    parser.add_argument('--taker-fee-bps', type=float, default=10.0)
    parser.add_argument('--slippage-bps', type=float, default=2.0)
    args = parser.parse_args()

    # Create results directory
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    results_dir = Path('results') / timestamp
    results_dir.mkdir(parents=True, exist_ok=True)

    config = {
        'timestamp': timestamp,
        'taker_fee_bps': args.taker_fee_bps,
        'slippage_bps': args.slippage_bps,
        'fixture': args.fixture,
        'mcap': args.mcap,
        'n': args.n,
        'strategy': 'ema_hourly_continuation'
    }
    with open(results_dir / 'config.json', 'w') as f:
        json.dump(config, f, indent=2)

    # Load universe
    if args.mcap:
        try:
            symbols = load_mcap_ranking(args.mcap)[:args.n]
        except Exception as e:
            print(f"Error loading mcap: {e}")
            symbols = ['BTC/USDT']
    else:
        default_mcap = Path('universe') / 'mcap_rank.json'
        if not default_mcap.exists():
            save_mcap_ranking(['BTC/USDT', 'ETH/USDT', 'SOL/USDT'], default_mcap)
        symbols = load_mcap_ranking(default_mcap)[:args.n]

    # Load data
    if args.fixture:
        df = load_ohlcv_csv(args.fixture)
    else:
        fixture_path = Path('data') / 'fixtures' / 'sample_hourly.csv'
        fixture_path.parent.mkdir(parents=True, exist_ok=True)
        if not fixture_path.exists():
            dates = pd.date_range('2024-01-01', periods=200, freq='h')
            np.random.seed(42)
            price = [100 + i * 0.01 + (i % 20 - 10) * 0.1 for i in range(200)]
            df_fix = pd.DataFrame({
                'timestamp': dates,
                'open': price,
                'high': [p + 0.3 for p in price],
                'low': [p - 0.3 for p in price],
                'close': price,
                'volume': 1000
            })
            df_fix.to_csv(fixture_path, index=False)
        df = load_ohlcv_csv(fixture_path)

    all_trades = []
    all_equity = []

    for symbol in symbols:
        df_sig = generate_signals(df.copy())
        trades, equity_df = backtest_symbol(
            df_sig,
            symbol=symbol,
            taker_fee_bps=args.taker_fee_bps,
            slippage_bps=args.slippage_bps
        )
        all_trades.extend(trades)
        all_equity.append(equity_df)

    # Pool equity - use average
    if all_equity:
        equity_result = all_equity[0].copy()
        equity_vals = np.mean([eq['equity'].values for eq in all_equity], axis=0)
        equity_result['equity'] = equity_vals
    else:
        equity_result = pd.DataFrame(columns=['timestamp', 'equity'])

    # Save trades
    trades_df = pd.DataFrame([t.__dict__ for t in all_trades])
    trades_df.to_csv(results_dir / 'trades.csv', index=False)

    # Save equity
    equity_result.to_csv(results_dir / 'equity.csv', index=False)

    # Calculate metrics
    metrics = calculate_metrics(all_trades, equity_result, symbol='pooled')
    metrics['per_symbol'] = {}

    for i, symbol in enumerate(symbols):
        sym_trades = [t for t in all_trades if t.symbol == symbol]
        if all_equity:
            sym_metrics = calculate_metrics(sym_trades, all_equity[i], symbol=symbol)
            metrics['per_symbol'][symbol] = sym_metrics

    # Save summary
    with open(results_dir / 'summary.json', 'w') as f:
        json.dump(metrics, f, indent=2, default=str)

    # Save markdown summary
    with open(results_dir / 'summary.md', 'w') as f:
        f.write('# EMA Hourly Continuation - Baseline Results\n\n')
        f.write(f'**Timestamp:** {timestamp}\n\n')
        f.write('## Pooled Metrics\n\n')
        f.write('| Metric | Value |\n|---|---|\n')
        f.write(f"| Trade Count | {metrics.get('trade_count', 0)} |\n")
        f.write(f"| Gross Profit Factor | {metrics.get('gross_profit_factor', 0):.4f} |\n")
        f.write(f"| Net Profit Factor | {metrics.get('net_profit_factor', 0):.4f} |\n")
        f.write(f"| Gross Win Rate | {metrics.get('gross_win_rate', 0):.4f} |\n")
        f.write(f"| Net Win Rate | {metrics.get('net_win_rate', 0):.4f} |\n")
        f.write(f"| Max Drawdown | {metrics.get('max_drawdown', 0):.4f} |\n")
        f.write(f"| Sharpe Ratio | {metrics.get('sharpe_ratio', 0):.4f} |\n")
        f.write(f"| Sortino Ratio | {metrics.get('sortino_ratio', 0):.4f} |\n")
        f.write(f"| CAGR | {metrics.get('cagr', 0):.4f} |\n\n")
        f.write('## Processing\n\n')
        f.write(f'- Processed in market cap descending order: {", ".join(symbols)}\n')
        f.write(f'- Costs: {args.taker_fee_bps} bps taker + {args.slippage_bps} bps slippage per side\n')

    print(f'Results saved to {results_dir}')
    print(f'Trades: {len(all_trades)}')


if __name__ == '__main__':
    main()
