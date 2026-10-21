# EMA Hourly Continuation — AEVO/USDT P12_55

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.7632 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9521 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -2.4076 |
| sortino_ratio | -0.8855 |
| max_drawdown | 0.6725 |
| cagr | -0.3350 |
| net_avg_win | 64.1401 |
| net_avg_loss | -78.9074 |
| avg_hold_time_bars | 11.8096 |
| exposure | 0.3564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
