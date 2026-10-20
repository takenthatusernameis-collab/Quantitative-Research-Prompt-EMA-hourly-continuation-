# EMA Hourly Continuation — BIGTIME/USDT P55_100

**Symbol:** BIGTIME/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.6325 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 1.0289 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -4.0026 |
| sortino_ratio | -1.3861 |
| max_drawdown | 0.8228 |
| cagr | -0.4824 |
| net_avg_win | 48.4138 |
| net_avg_loss | -70.2049 |
| avg_hold_time_bars | 5.9086 |
| exposure | 0.1610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
