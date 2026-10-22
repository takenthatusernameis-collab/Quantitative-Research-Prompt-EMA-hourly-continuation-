# EMA Hourly Continuation — DBR/USDT P8_12

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1093 |
| net_profit_factor | 0.3180 |
| net_win_rate | 0.3724 |
| gross_profit_factor | 0.9100 |
| gross_win_rate | 0.4355 |
| sharpe_ratio | -14.9802 |
| sortino_ratio | -7.9947 |
| max_drawdown | 0.9998 |
| cagr | -0.9863 |
| net_avg_win | 11.4545 |
| net_avg_loss | -21.3705 |
| avg_hold_time_bars | 3.2919 |
| exposure | 0.2046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
