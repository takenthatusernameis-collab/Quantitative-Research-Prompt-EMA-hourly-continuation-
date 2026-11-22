# EMA Hourly Continuation — AZERO/USDT P21_50

**Symbol:** AZERO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 882 |
| net_profit_factor | 0.5244 |
| net_win_rate | 0.4342 |
| gross_profit_factor | 0.9389 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -6.6801 |
| sortino_ratio | -2.7729 |
| max_drawdown | 0.9691 |
| cagr | -0.7435 |
| net_avg_win | 27.8613 |
| net_avg_loss | -40.7772 |
| avg_hold_time_bars | 5.7630 |
| exposure | 0.2300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
