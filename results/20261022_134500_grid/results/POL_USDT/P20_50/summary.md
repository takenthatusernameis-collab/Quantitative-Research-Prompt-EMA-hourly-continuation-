# EMA Hourly Continuation — POL/USDT P20_50

**Symbol:** POL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1041 |
| net_profit_factor | 0.4003 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.7960 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -8.1877 |
| sortino_ratio | -3.7316 |
| max_drawdown | 0.9902 |
| cagr | -0.8415 |
| net_avg_win | 14.3700 |
| net_avg_loss | -28.4204 |
| avg_hold_time_bars | 5.1105 |
| exposure | 0.2418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
