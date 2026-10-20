# EMA Hourly Continuation — LQTY/USDT P89_100

**Symbol:** LQTY/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.2828 |
| net_win_rate | 0.4006 |
| gross_profit_factor | 0.7198 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -8.3551 |
| sortino_ratio | -2.9651 |
| max_drawdown | 0.9776 |
| cagr | -0.7778 |
| net_avg_win | 15.5443 |
| net_avg_loss | -36.7389 |
| avg_hold_time_bars | 2.5218 |
| exposure | 0.0706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
