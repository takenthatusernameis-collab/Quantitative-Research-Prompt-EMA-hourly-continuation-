# EMA Hourly Continuation — MAGIC/USDT P8_55

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.7890 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 1.0117 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -2.2980 |
| sortino_ratio | -0.8588 |
| max_drawdown | 0.6592 |
| cagr | -0.3265 |
| net_avg_win | 69.4430 |
| net_avg_loss | -86.7297 |
| avg_hold_time_bars | 15.9488 |
| exposure | 0.4951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
