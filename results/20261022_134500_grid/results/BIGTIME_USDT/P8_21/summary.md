# EMA Hourly Continuation — BIGTIME/USDT P8_21

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1503 |
| net_profit_factor | 0.4809 |
| net_win_rate | 0.4385 |
| gross_profit_factor | 0.8784 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -9.9640 |
| sortino_ratio | -5.4080 |
| max_drawdown | 0.9989 |
| cagr | -0.9319 |
| net_avg_win | 14.0440 |
| net_avg_loss | -22.8005 |
| avg_hold_time_bars | 3.5961 |
| exposure | 0.2446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
