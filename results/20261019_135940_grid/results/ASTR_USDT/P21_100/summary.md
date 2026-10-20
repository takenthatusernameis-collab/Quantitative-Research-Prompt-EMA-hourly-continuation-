# EMA Hourly Continuation — ASTR/USDT P21_100

**Symbol:** ASTR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.6535 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 1.0031 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -3.2731 |
| sortino_ratio | -1.1186 |
| max_drawdown | 0.7580 |
| cagr | -0.4113 |
| net_avg_win | 48.4543 |
| net_avg_loss | -70.9302 |
| avg_hold_time_bars | 16.6354 |
| exposure | 0.4419 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
