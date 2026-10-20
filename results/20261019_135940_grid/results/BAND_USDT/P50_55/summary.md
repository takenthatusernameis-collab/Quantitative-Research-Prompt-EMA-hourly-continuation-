# EMA Hourly Continuation — BAND/USDT P50_55

**Symbol:** BAND/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.3297 |
| net_win_rate | 0.3886 |
| gross_profit_factor | 0.9753 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -10.4813 |
| sortino_ratio | -4.1557 |
| max_drawdown | 0.9963 |
| cagr | -0.8894 |
| net_avg_win | 16.7219 |
| net_avg_loss | -32.2360 |
| avg_hold_time_bars | 2.7865 |
| exposure | 0.0951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
