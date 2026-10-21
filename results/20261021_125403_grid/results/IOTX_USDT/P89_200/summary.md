# EMA Hourly Continuation — IOTX/USDT P89_200

**Symbol:** IOTX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7840 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 0.9992 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.2495 |
| sortino_ratio | -0.3151 |
| max_drawdown | 0.3544 |
| cagr | -0.1356 |
| net_avg_win | 71.3290 |
| net_avg_loss | -92.1593 |
| avg_hold_time_bars | 14.9871 |
| exposure | 0.2112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
