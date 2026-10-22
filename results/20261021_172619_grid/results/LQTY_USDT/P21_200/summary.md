# EMA Hourly Continuation — LQTY/USDT P21_200

**Symbol:** LQTY/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7638 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9229 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.3408 |
| sortino_ratio | -0.3326 |
| max_drawdown | 0.3498 |
| cagr | -0.1424 |
| net_avg_win | 70.2057 |
| net_avg_loss | -87.2005 |
| avg_hold_time_bars | 47.6974 |
| exposure | 0.6561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
