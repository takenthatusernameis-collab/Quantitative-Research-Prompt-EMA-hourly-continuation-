# EMA Hourly Continuation — POLYX/USDT P144_200

**Symbol:** POLYX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.4495 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8840 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -4.4908 |
| sortino_ratio | -1.2794 |
| max_drawdown | 0.7952 |
| cagr | -0.4630 |
| net_avg_win | 34.3204 |
| net_avg_loss | -65.5431 |
| avg_hold_time_bars | 5.1204 |
| exposure | 0.0947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
