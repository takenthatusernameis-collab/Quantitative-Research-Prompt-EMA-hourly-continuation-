# EMA Hourly Continuation — CHZ/USDT P8_12

**Symbol:** CHZ/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1910 |
| net_profit_factor | 0.2448 |
| net_win_rate | 0.3565 |
| gross_profit_factor | 0.7811 |
| gross_win_rate | 0.4152 |
| sharpe_ratio | -19.1488 |
| sortino_ratio | -12.1573 |
| max_drawdown | 1.0000 |
| cagr | -0.9986 |
| net_avg_win | 4.7595 |
| net_avg_loss | -10.7740 |
| avg_hold_time_bars | 1.8120 |
| exposure | 0.1573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
