# EMA Hourly Continuation — ROSE/USDT P21_34

**Symbol:** ROSE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.6142 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8420 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -2.7717 |
| sortino_ratio | -0.7170 |
| max_drawdown | 0.5781 |
| cagr | -0.2791 |
| net_avg_win | 59.4807 |
| net_avg_loss | -81.1522 |
| avg_hold_time_bars | 5.0547 |
| exposure | 0.0756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
