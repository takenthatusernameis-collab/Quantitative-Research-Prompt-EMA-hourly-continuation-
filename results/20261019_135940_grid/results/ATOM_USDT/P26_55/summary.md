# EMA Hourly Continuation — ATOM/USDT P26_55

**Symbol:** ATOM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 860 |
| net_profit_factor | 0.3810 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.7762 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -7.4802 |
| sortino_ratio | -3.1202 |
| max_drawdown | 0.9790 |
| cagr | -0.7818 |
| net_avg_win | 15.6790 |
| net_avg_loss | -33.1977 |
| avg_hold_time_bars | 4.3907 |
| exposure | 0.1716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
