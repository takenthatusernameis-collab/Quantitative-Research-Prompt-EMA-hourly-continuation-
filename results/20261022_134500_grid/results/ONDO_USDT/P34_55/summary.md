# EMA Hourly Continuation — ONDO/USDT P34_55

**Symbol:** ONDO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 872 |
| net_profit_factor | 0.4438 |
| net_win_rate | 0.4323 |
| gross_profit_factor | 0.8400 |
| gross_win_rate | 0.4415 |
| sharpe_ratio | -8.1098 |
| sortino_ratio | -3.3868 |
| max_drawdown | 0.9859 |
| cagr | -0.8151 |
| net_avg_win | 20.8558 |
| net_avg_loss | -35.7948 |
| avg_hold_time_bars | 2.9472 |
| exposure | 0.1168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
