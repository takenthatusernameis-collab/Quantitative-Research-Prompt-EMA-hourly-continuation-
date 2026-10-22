# EMA Hourly Continuation — AXS/USDT P26_200

**Symbol:** AXS/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.8377 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1544 |
| gross_win_rate | 0.5360 |
| sharpe_ratio | -1.0661 |
| sortino_ratio | -0.2831 |
| max_drawdown | 0.3537 |
| cagr | -0.1255 |
| net_avg_win | 80.0580 |
| net_avg_loss | -109.1390 |
| avg_hold_time_bars | 36.7925 |
| exposure | 0.5777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
