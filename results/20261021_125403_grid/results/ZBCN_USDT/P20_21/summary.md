# EMA Hourly Continuation — ZBCN/USDT P20_21

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 97 |
| net_profit_factor | 0.9854 |
| net_win_rate | 0.5567 |
| gross_profit_factor | 1.2443 |
| gross_win_rate | 0.5567 |
| sharpe_ratio | -0.0160 |
| sortino_ratio | -0.0023 |
| max_drawdown | 0.0877 |
| cagr | -0.0030 |
| net_avg_win | 90.8133 |
| net_avg_loss | -115.7374 |
| avg_hold_time_bars | 5.7113 |
| exposure | 0.0256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
