# EMA Hourly Continuation — POLYX/USDT P21_26

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.6301 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 1.0145 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -2.7090 |
| sortino_ratio | -0.6799 |
| max_drawdown | 0.5680 |
| cagr | -0.2683 |
| net_avg_win | 61.7458 |
| net_avg_loss | -95.4436 |
| avg_hold_time_bars | 4.5559 |
| exposure | 0.0630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
