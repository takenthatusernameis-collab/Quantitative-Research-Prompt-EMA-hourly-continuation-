# EMA Hourly Continuation — ZBCN/USDT P21_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.9094 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0703 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -0.5963 |
| sortino_ratio | -0.1935 |
| max_drawdown | 0.2725 |
| cagr | -0.0906 |
| net_avg_win | 80.6825 |
| net_avg_loss | -96.1118 |
| avg_hold_time_bars | 13.8380 |
| exposure | 0.3201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
