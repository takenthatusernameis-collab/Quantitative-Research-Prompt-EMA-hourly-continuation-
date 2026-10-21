# EMA Hourly Continuation — AR/USDT P8_100

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.8596 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 1.0004 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -0.9009 |
| sortino_ratio | -0.2593 |
| max_drawdown | 0.2852 |
| cagr | -0.1156 |
| net_avg_win | 80.1052 |
| net_avg_loss | -94.1130 |
| avg_hold_time_bars | 38.4728 |
| exposure | 0.7065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
