# EMA Hourly Continuation — MNT/USDT P21_200

**Symbol:** MNT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.6723 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 0.9933 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -1.8941 |
| sortino_ratio | -0.4850 |
| max_drawdown | 0.4890 |
| cagr | -0.2059 |
| net_avg_win | 54.6578 |
| net_avg_loss | -81.7919 |
| avg_hold_time_bars | 43.9939 |
| exposure | 0.6579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
