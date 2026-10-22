# EMA Hourly Continuation — LQTY/USDT P89_200

**Symbol:** LQTY/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7565 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9568 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -1.4459 |
| sortino_ratio | -0.3634 |
| max_drawdown | 0.3567 |
| cagr | -0.1539 |
| net_avg_win | 69.8251 |
| net_avg_loss | -89.9542 |
| avg_hold_time_bars | 13.6645 |
| exposure | 0.1917 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
