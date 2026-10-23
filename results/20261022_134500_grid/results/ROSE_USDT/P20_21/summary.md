# EMA Hourly Continuation — ROSE/USDT P20_21

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1325 |
| net_profit_factor | 0.1360 |
| net_win_rate | 0.3140 |
| gross_profit_factor | 0.6413 |
| gross_win_rate | 0.3932 |
| sharpe_ratio | -17.6963 |
| sortino_ratio | -9.6092 |
| max_drawdown | 1.0000 |
| cagr | -0.9956 |
| net_avg_win | 3.7841 |
| net_avg_loss | -12.7329 |
| avg_hold_time_bars | 1.6475 |
| exposure | 0.0992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
