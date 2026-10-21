# EMA Hourly Continuation — KAS/USDT P50_55

**Symbol:** KAS/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 76 |
| net_profit_factor | 0.6571 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9314 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.0703 |
| sortino_ratio | -0.1339 |
| max_drawdown | 0.1813 |
| cagr | -0.0586 |
| net_avg_win | 72.8617 |
| net_avg_loss | -105.2045 |
| avg_hold_time_bars | 5.6447 |
| exposure | 0.0195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
