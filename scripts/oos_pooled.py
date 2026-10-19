#!/usr/bin/env python3
"""Pooled cross-symbol out-of-sample backtest with per-symbol aggregation.

For each symbol:
  - chronological train/test split (test = trailing test_fraction, default 35%)
  - EMA/signal computed on the full series (causal EMA, no lookahead into future)
  - entries only taken in the test window (entry_start_index = cut)
  - per-symbol metrics + pooled trades/equity aggregation

Reports per-symbol and pooled net/gross metrics and signal sparsity.
"""
import argparse
import json
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import numpy as np

from data.data_loader import load_ohlcv_csv
from signals.signals import generate_signals
from universe.universe import load_mcap_ranking
from backtest.backtest import backtest_symbol
from metrics.metrics import calculate_metrics


def run_symbol(symbol, df, test_fraction, taker_fee_bps, slippage_bps,
               rr, stricter_trend, min_risk_atr, atr_threshold, conservative_exit=True,
               sizing='risk', risk_fraction=0.01, max_notional_multiple=10.0):
    n = len(df)
    cut = int(n * (1.0 - test_fraction))
    if cut < 1:
        cut = 1
    test = df.iloc[cut:].copy()
    train = df.iloc[:cut].copy()

    # Signals on full series (causal). Restrict entries to test window via
    # entry_start_index so EMA warmup can use train history but no test-bar
    # entries leak into train.
    df_sig = generate_signals(df.copy(),
                              stricter_trend=stricter_trend)

    # Signal counts in train vs test (sparsity diagnostic)
    train_sigs = int((df_sig['signal'].iloc[:cut] != 0).sum())
    test_sigs = int((df_sig['signal'].iloc[cut:] != 0).sum())

    trades, equity_df = backtest_symbol(
        df_sig, symbol=symbol,
        taker_fee_bps=taker_fee_bps, slippage_bps=slippage_bps, rr=rr,
        min_risk_atr=min_risk_atr, atr_threshold=atr_threshold,
        entry_start_index=cut, conservative_exit=conservative_exit,
        sizing=sizing, risk_fraction=risk_fraction,
        max_notional_multiple=max_notional_multiple,
    )

    # Restrict equity curve to test window for test-window metrics
    test_equity = equity_df.iloc[cut:].copy() if len(equity_df) > cut else equity_df

    sym_metrics = calculate_metrics(trades, test_equity, symbol=symbol)
    sym_metrics['train_bars'] = len(train)
    sym_metrics['test_bars'] = len(test)
    sym_metrics['train_signals'] = train_sigs
    sym_metrics['test_signals'] = test_sigs
    sym_metrics['test_fraction'] = test_fraction
    return trades, test_equity, sym_metrics, train, test


def main():
    parser = argparse.ArgumentParser(description='Pooled cross-symbol OOS backtest')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--n', type=int, default=5)
    parser.add_argument('--test-fraction', type=float, default=0.35,
                        help='Trailing OOS test fraction (e.g. 0.30-0.40)')
    parser.add_argument('--taker-fee-bps', type=float, default=10.0)
    parser.add_argument('--slippage-bps', type=float, default=2.0)
    parser.add_argument('--rr', type=float, default=1.5)
    parser.add_argument('--stricter-trend', action='store_true', default=False)
    parser.add_argument('--min-risk-atr', action='store_true', default=True)
    parser.add_argument('--atr-threshold', type=float, default=0.75)
    parser.add_argument('--sizing', type=str, default='risk', choices=['risk', 'unit_notional'])
    parser.add_argument('--risk-fraction', type=float, default=0.01)
    parser.add_argument('--max-notional-multiple', type=float, default=10.0)
    args = parser.parse_args()

    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    results_dir = Path('results') / f'{timestamp}_oos_pooled'
    results_dir.mkdir(parents=True, exist_ok=True)

    symbols = load_mcap_ranking(args.mcap)[:args.n]

    run_config = {
        'timestamp': timestamp,
        'strategy': 'ema_hourly_continuation',
        'mode': 'pooled_cross_symbol_oos',
        'test_fraction': args.test_fraction,
        'taker_fee_bps': args.taker_fee_bps,
        'slippage_bps': args.slippage_bps,
        'rr': args.rr,
        'stricter_trend': args.stricter_trend,
        'min_risk_atr': args.min_risk_atr,
        'atr_threshold': args.atr_threshold,
        'conservative_exit': not args.aggressive_exit,
        'sizing': args.sizing,
        'risk_fraction': args.risk_fraction,
        'max_notional_multiple': args.max_notional_multiple,
        'symbols': symbols,
        'source_config': 'config/default.json',
    }
    with open(results_dir / 'config.json', 'w') as f:
        json.dump(run_config, f, indent=2)

    all_trades = []
    per_symbol = {}
    for symbol in symbols:
        sym_file = Path(args.fixture_base) / f'{symbol.replace("/", "_")}.csv'
        if not sym_file.exists():
            print(f'SKIP {symbol}: no fixture {sym_file}')
            continue
        df = load_ohlcv_csv(str(sym_file))
        trades, test_equity, sym_metrics, train, test = run_symbol(
            symbol, df, args.test_fraction, args.taker_fee_bps, args.slippage_bps,
            args.rr, args.stricter_trend, args.min_risk_atr, args.atr_threshold,
            conservative_exit=not args.aggressive_exit,
        )
        all_trades.extend(trades)
        per_symbol[symbol] = sym_metrics
        print(f'{symbol}: train={sym_metrics["train_bars"]} test={sym_metrics["test_bars"]} '
              f'train_sigs={sym_metrics["train_signals"]} test_sigs={sym_metrics["test_signals"]} '
              f'trades={sym_metrics["trade_count"]} netPF={sym_metrics.get("net_profit_factor",0):.4f} '
              f'netSharpe={sym_metrics.get("sharpe_ratio",0):.4f}')

    # Pooled equity: average across symbols' test equity curves (aligned by index)
    test_equities = []
    for symbol in symbols:
        if symbol not in per_symbol:
            continue
        # Re-load to rebuild test equity for pooling alignment
        sym_file = Path(args.fixture_base) / f'{symbol.replace("/", "_")}.csv'
        df = load_ohlcv_csv(str(sym_file))
        cut = int(len(df) * (1.0 - args.test_fraction))
        _, te, _, _, _ = run_symbol(symbol, df, args.test_fraction, args.taker_fee_bps,
                                    args.slippage_bps, args.rr, args.stricter_trend,
                                    args.min_risk_atr, args.atr_threshold,
                                    conservative_exit=not args.aggressive_exit)
        if len(te) > 0:
            test_equities.append(te)

    if test_equities:
        min_len = min(len(eq) for eq in test_equities)
        equity_result = test_equities[0].iloc[:min_len].copy()
        equity_vals = np.mean([eq['equity'].values[:min_len] for eq in test_equities], axis=0)
        equity_result['equity'] = equity_vals
    else:
        equity_result = pd.DataFrame(columns=['timestamp', 'equity'])

    pooled_metrics = calculate_metrics(all_trades, equity_result, symbol='pooled')
    pooled_metrics['n_symbols'] = len(per_symbol)
    pooled_metrics['test_fraction'] = args.test_fraction

    # Save trades
    trades_df = pd.DataFrame([t.__dict__ for t in all_trades])
    trades_df.to_csv(results_dir / 'trades.csv', index=False)
    equity_result.to_csv(results_dir / 'equity.csv', index=False)

    summary = {
        'config': run_config,
        'pooled': pooled_metrics,
        'per_symbol': per_symbol,
    }
    with open(results_dir / 'summary.json', 'w') as f:
        json.dump(summary, f, indent=2, default=str)

    # Markdown report
    lines = []
    lines.append('# Pooled Cross-Symbol OOS — EMA Hourly Continuation\n')
    lines.append(f'**Timestamp:** {timestamp}\n')
    lines.append(f'**Mode:** pooled cross-symbol out-of-sample (test = trailing {args.test_fraction:.0%} of each symbol)\n')
    lines.append(f'**Symbols (market-cap desc):** {", ".join(symbols)}\n')
    lines.append(f'**Config:** rr={args.rr}, min_risk_atr={args.min_risk_atr}, atr_threshold={args.atr_threshold}, '
                 f'stricter_trend={args.stricter_trend}, costs={args.taker_fee_bps}bps+{args.slippage_bps}bps per side\n')
    lines.append('\n## Pooled OOS Metrics\n')
    lines.append('| Metric | Value |\n|---|---|')
    for k in ['trade_count', 'net_profit_factor', 'net_win_rate', 'gross_profit_factor',
              'gross_win_rate', 'sharpe_ratio', 'sortino_ratio', 'max_drawdown', 'cagr',
              'net_avg_win', 'net_avg_loss', 'avg_hold_time_bars', 'exposure', 'n_symbols']:
        v = pooled_metrics.get(k)
        lines.append(f'| {k} | {v:.4f} |' if isinstance(v, float) else f'| {k} | {v} |')
    lines.append('\n## Per-Symbol OOS Metrics (market-cap order)\n')
    lines.append('| Symbol | Test Bars | Test Signals | Trades | Net PF | Net WR | Net Sharpe | Max DD |')
    lines.append('|---|---|---|---|---|---|---|---|')
    for symbol in symbols:
        m = per_symbol.get(symbol, {})
        lines.append(f'| {symbol} | {m.get("test_bars","-")} | {m.get("test_signals","-")} | '
                     f'{m.get("trade_count","-")} | {m.get("net_profit_factor",0):.4f} | '
                     f'{m.get("net_win_rate",0):.4f} | {m.get("sharpe_ratio",0):.4f} | '
                     f'{m.get("max_drawdown",0):.4f} |')
    lines.append('\n## Signal Sparsity\n')
    lines.append('Most OOS windows produce few/no qualifying signals (EMA stack + pullback cross + ATR min-risk filter). '
                 'With 500-bar fixtures (~21 days) and a 35% test split, each test window is ~175 bars; after the 100-bar '
                 'EMA warmup the effective OOS sample is short, which limits trade counts and the statistical power of OOS metrics.\n')

    with open(results_dir / 'summary.md', 'w') as f:
        f.write('\n'.join(lines))

    print(f'\nResults saved to {results_dir}')
    print(f'Pooled OOS trades: {pooled_metrics.get("trade_count")} netPF={pooled_metrics.get("net_profit_factor",0):.4f} '
          f'netSharpe={pooled_metrics.get("sharpe_ratio",0):.4f}')


if __name__ == '__main__':
    main()
