# EMA Hourly Continuation — KAVA/USDT P21_55

**Symbol:** KAVA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 998 |
| net_profit_factor | 0.5310 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.9983 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -8.3462 |
| sortino_ratio | -3.7269 |
| max_drawdown | 0.9910 |
| cagr | -0.8448 |
| net_avg_win | 25.5544 |
| net_avg_loss | -37.7916 |
| avg_hold_time_bars | 5.7545 |
| exposure | 0.2610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
