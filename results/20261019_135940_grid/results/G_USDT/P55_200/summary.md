# EMA Hourly Continuation — G/USDT P55_200

**Symbol:** G/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.5937 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8746 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -3.1126 |
| sortino_ratio | -0.8524 |
| max_drawdown | 0.6167 |
| cagr | -0.3307 |
| net_avg_win | 57.0498 |
| net_avg_loss | -81.8136 |
| avg_hold_time_bars | 22.1111 |
| exposure | 0.3767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
