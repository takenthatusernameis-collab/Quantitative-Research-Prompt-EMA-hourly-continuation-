# EMA Hourly Continuation — PROM/USDT P20_100

**Symbol:** PROM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.4838 |
| net_win_rate | 0.4181 |
| gross_profit_factor | 0.8244 |
| gross_win_rate | 0.4440 |
| sharpe_ratio | -6.2425 |
| sortino_ratio | -2.2968 |
| max_drawdown | 0.9433 |
| cagr | -0.6759 |
| net_avg_win | 30.3101 |
| net_avg_loss | -45.0121 |
| avg_hold_time_bars | 13.3448 |
| exposure | 0.4222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
