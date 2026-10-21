# EMA Hourly Continuation — LQTY/USDT P20_55

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.7298 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9529 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.2927 |
| sortino_ratio | -0.7826 |
| max_drawdown | 0.6083 |
| cagr | -0.3012 |
| net_avg_win | 57.1996 |
| net_avg_loss | -75.9441 |
| avg_hold_time_bars | 10.2452 |
| exposure | 0.2647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
