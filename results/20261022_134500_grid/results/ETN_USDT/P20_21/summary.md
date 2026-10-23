# EMA Hourly Continuation — ETN/USDT P20_21

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1092 |
| net_profit_factor | 0.0958 |
| net_win_rate | 0.2051 |
| gross_profit_factor | 0.2365 |
| gross_win_rate | 0.2518 |
| sharpe_ratio | -21.2215 |
| sortino_ratio | -11.7932 |
| max_drawdown | 1.0000 |
| cagr | -0.9988 |
| net_avg_win | 4.7281 |
| net_avg_loss | -12.7409 |
| avg_hold_time_bars | 2.0659 |
| exposure | 0.1225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
