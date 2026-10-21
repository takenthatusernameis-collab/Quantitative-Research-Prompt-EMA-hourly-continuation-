# EMA Hourly Continuation — AERO/USDT P21_100

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.8886 |
| net_win_rate | 0.5116 |
| gross_profit_factor | 1.0476 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -0.7841 |
| sortino_ratio | -0.2340 |
| max_drawdown | 0.3214 |
| cagr | -0.1057 |
| net_avg_win | 88.2394 |
| net_avg_loss | -104.0124 |
| avg_hold_time_bars | 18.3912 |
| exposure | 0.3611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
