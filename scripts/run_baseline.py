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

CONFIG_DEFAULTS = {
    'ema_fast': 50,
    'ema_slow': 100,
    'rr': 1.0,
    'taker_fee_bps': 10.0,
    'slippage_bps': 2.0,
    'warmup_bars': 100,
    'risk_pathological_threshold': 1e-10,
    'min_risk_atr': False,
    'atr_threshold': 1.0,
    'stricter_trend': False,
}

REQUIRED_CONFIG_KEYS = {'ema_fast', 'ema_slow', 'taker_fee_bps', 'slippage_bps', 'rr'}


def load_config(path: str | Path | None) -> dict:
    """Load config from JSON file, merging with defaults."""
    config = dict(CONFIG_DEFAULTS)
    if path is None:
        return config
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with path.open('r') as f:
        file_config = json.load(f)
    if not isinstance(file_config, dict):
        raise ValueError(f"Config file {path} must contain a JSON object")
    missing = REQUIRED_CONFIG_KEYS - set(file_config.keys())
    if missing:
        raise ValueError(f"Config missing required keys: {sorted(missing)}")
    config.update(file_config)
    return config


def main():
    parser = argparse.ArgumentParser(description='Run EMA hourly continuation baseline')
    parser.add_argument('--fixture', type=str, help='Path to CSV fixture')
    parser.add_argument('--mcap', type=str, help='Path to mcap ranking JSON')
    parser.add_argument('--config', type=str, help='Path to JSON config file')
    parser.add_argument('--n', type=int, default=3, help='Number of symbols to process')
    parser.add_argument('--taker-fee-bps', type=float, default=None)
    parser.add_argument('--slippage-bps', type=float, default=None)
    parser.add_argument('--rr', type=float, default=None)
    parser.add_argument('--stricter-trend', action='store_true', default=None)
    parser.add_argument('--min-risk-atr', action='store_true', default=None)
    parser.add_argument('--atr-threshold', type=float, default=None)
    args = parser.parse_args()

    config = load_config(args.config)

    # CLI args override config values
    if args.taker_fee_bps is not None:
        config['taker_fee_bps'] = args.taker_fee_bps
    if args.slippage_bps is not None:
        config['slippage_bps'] = args.slippage_bps
    if args.rr is not None:
        config['rr'] = args.rr
    if args.stricter_trend is not None:
        config['stricter_trend'] = args.stricter_trend
    if args.min_risk_atr is not None:
        config['min_risk_atr'] = args.min_risk_atr
    if args.atr_threshold is not None:
        config['atr_threshold'] = args.atr_threshold

    taker_fee_bps = float(config['taker_fee_bps'])
    slippage_bps = float(config['slippage_bps'])
    ema_fast = int(config['ema_fast'])
    ema_slow = int(config['ema_slow'])
    rr = float(config.get('rr', 1.0))
    stricter_trend = bool(config.get('stricter_trend', False))
    min_risk_atr = bool(config.get('min_risk_atr', False))
    atr_threshold = float(config.get('atr_threshold', 1.0))

    # Create results directory
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    results_dir = Path('results') / timestamp
    results_dir.mkdir(parents=True, exist_ok=True)

    run_config = {
        'timestamp': timestamp,
        'taker_fee_bps': taker_fee_bps,
        'slippage_bps': slippage_bps,
        'ema_fast': ema_fast,
        'ema_slow': ema_slow,
        'rr': rr,
        'stricter_trend': stricter_trend,
        'min_risk_atr': min_risk_atr,
        'atr_threshold': atr_threshold,
        'fixture': args.fixture,
        'mcap': args.mcap,
        'config': args.config,
        'n': args.n,
        'strategy': 'ema_hourly_continuation',
        'source_config': dict(config),
    }
    with open(results_dir / 'config.json', 'w') as f:
        json.dump(run_config, f, indent=2)

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
    fixture_base = Path('data') / 'fixtures'
    all_trades = []
    all_equity = []

    for symbol in symbols:
        sym_file = fixture_base / f'{symbol.replace("/", "_")}.csv'
        if args.fixture:
            # if single fixture passed, maybe use it for all? but better to use per-symbol if exists
            df = load_ohlcv_csv(args.fixture)
        elif sym_file.exists():
            df = load_ohlcv_csv(sym_file)
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
        df_sig = generate_signals(df.copy(), stricter_trend=stricter_trend)
        trades, equity_df = backtest_symbol(
            df_sig,
            symbol=symbol,
            taker_fee_bps=taker_fee_bps,
            slippage_bps=slippage_bps,
            rr=rr,
            min_risk_atr=min_risk_atr,
            atr_threshold=atr_threshold
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
        f.write(f'- Costs: {taker_fee_bps} bps taker + {slippage_bps} bps slippage per side\n')

    print(f'Results saved to {results_dir}')
    print(f'Trades: {len(all_trades)}')


if __name__ == '__main__':
    main()
