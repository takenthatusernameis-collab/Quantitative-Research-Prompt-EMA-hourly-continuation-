# EMA Hourly Continuation — CHZ/USDT P21_55

**Symbol:** CHZ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.7712 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 1.0279 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -2.0145 |
| sortino_ratio | -0.6547 |
| max_drawdown | 0.5559 |
| cagr | -0.2596 |
| net_avg_win | 69.4871 |
| net_avg_loss | -90.4571 |
| avg_hold_time_bars | 8.0565 |
| exposure | 0.1879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
