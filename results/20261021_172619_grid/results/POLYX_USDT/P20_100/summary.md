# EMA Hourly Continuation — POLYX/USDT P20_100

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7690 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9785 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.0352 |
| sortino_ratio | -0.6544 |
| max_drawdown | 0.5851 |
| cagr | -0.2615 |
| net_avg_win | 70.9573 |
| net_avg_loss | -89.4159 |
| avg_hold_time_bars | 17.8406 |
| exposure | 0.4120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
