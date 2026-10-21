# EMA Hourly Continuation — DOT/USDT P8_50

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.7664 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0012 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -2.1051 |
| sortino_ratio | -0.7744 |
| max_drawdown | 0.6265 |
| cagr | -0.2993 |
| net_avg_win | 58.7134 |
| net_avg_loss | -77.0812 |
| avg_hold_time_bars | 14.9742 |
| exposure | 0.4479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
