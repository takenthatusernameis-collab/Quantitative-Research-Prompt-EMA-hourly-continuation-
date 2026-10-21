# EMA Hourly Continuation — PHA/USDT P8_200

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.8785 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0215 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -0.7887 |
| sortino_ratio | -0.2092 |
| max_drawdown | 0.3573 |
| cagr | -0.0946 |
| net_avg_win | 92.3731 |
| net_avg_loss | -106.3741 |
| avg_hold_time_bars | 48.4390 |
| exposure | 0.7574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
