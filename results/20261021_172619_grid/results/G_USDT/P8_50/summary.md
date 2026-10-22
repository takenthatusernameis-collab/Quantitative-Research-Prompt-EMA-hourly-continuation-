# EMA Hourly Continuation — G/USDT P8_50

**Symbol:** G/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.7344 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -2.5652 |
| sortino_ratio | -0.9966 |
| max_drawdown | 0.6765 |
| cagr | -0.3674 |
| net_avg_win | 55.1216 |
| net_avg_loss | -74.1194 |
| avg_hold_time_bars | 14.2437 |
| exposure | 0.4763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
