# EMA Hourly Continuation — BIGTIME/USDT P21_50

**Symbol:** BIGTIME/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.7421 |
| net_win_rate | 0.5009 |
| gross_profit_factor | 0.9824 |
| gross_win_rate | 0.5009 |
| sharpe_ratio | -2.0962 |
| sortino_ratio | -0.6912 |
| max_drawdown | 0.5529 |
| cagr | -0.2714 |
| net_avg_win | 59.4893 |
| net_avg_loss | -80.4712 |
| avg_hold_time_bars | 9.3051 |
| exposure | 0.2236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
