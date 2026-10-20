# EMA Hourly Continuation — MAGIC/USDT P26_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.6895 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9187 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -2.3321 |
| sortino_ratio | -0.6283 |
| max_drawdown | 0.5708 |
| cagr | -0.2545 |
| net_avg_win | 68.1709 |
| net_avg_loss | -88.4583 |
| avg_hold_time_bars | 36.8417 |
| exposure | 0.6029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
