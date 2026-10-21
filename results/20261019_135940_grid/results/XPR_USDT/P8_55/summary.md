# EMA Hourly Continuation — XPR/USDT P8_55

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1105 |
| net_profit_factor | 0.4791 |
| net_win_rate | 0.4317 |
| gross_profit_factor | 0.8660 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -8.7481 |
| sortino_ratio | -4.0632 |
| max_drawdown | 0.9947 |
| cagr | -0.8732 |
| net_avg_win | 19.1706 |
| net_avg_loss | -30.3957 |
| avg_hold_time_bars | 8.8226 |
| exposure | 0.4431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
