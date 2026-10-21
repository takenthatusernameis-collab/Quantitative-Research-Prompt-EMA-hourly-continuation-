# EMA Hourly Continuation — BLUR/USDT P26_50

**Symbol:** BLUR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.6947 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 0.9613 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -2.1944 |
| sortino_ratio | -0.6893 |
| max_drawdown | 0.5861 |
| cagr | -0.2700 |
| net_avg_win | 51.7295 |
| net_avg_loss | -74.7763 |
| avg_hold_time_bars | 6.0561 |
| exposure | 0.1318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
