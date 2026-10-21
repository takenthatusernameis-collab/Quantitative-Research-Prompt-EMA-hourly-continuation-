# EMA Hourly Continuation — SUPER/USDT P21_55

**Symbol:** SUPER/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.8123 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0718 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -1.6084 |
| sortino_ratio | -0.5387 |
| max_drawdown | 0.5169 |
| cagr | -0.2209 |
| net_avg_win | 71.7595 |
| net_avg_loss | -94.3819 |
| avg_hold_time_bars | 8.0037 |
| exposure | 0.1979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
