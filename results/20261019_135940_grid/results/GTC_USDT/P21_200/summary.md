# EMA Hourly Continuation — GTC/USDT P21_200

**Symbol:** GTC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6576 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.8839 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -2.7148 |
| sortino_ratio | -0.7870 |
| max_drawdown | 0.6345 |
| cagr | -0.3075 |
| net_avg_win | 59.9642 |
| net_avg_loss | -77.1877 |
| avg_hold_time_bars | 31.1758 |
| exposure | 0.5966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
