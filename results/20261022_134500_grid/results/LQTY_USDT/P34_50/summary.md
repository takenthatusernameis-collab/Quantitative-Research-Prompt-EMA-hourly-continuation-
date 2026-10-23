# EMA Hourly Continuation — LQTY/USDT P34_50

**Symbol:** LQTY/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.3934 |
| net_win_rate | 0.4239 |
| gross_profit_factor | 0.8323 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -8.8600 |
| sortino_ratio | -3.8877 |
| max_drawdown | 0.9921 |
| cagr | -0.8515 |
| net_avg_win | 15.9191 |
| net_avg_loss | -29.7812 |
| avg_hold_time_bars | 3.1112 |
| exposure | 0.1342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
