# EMA Hourly Continuation — MTL/USDT P8_55

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 862 |
| net_profit_factor | 0.6237 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 1.0095 |
| gross_win_rate | 0.4849 |
| sharpe_ratio | -5.1465 |
| sortino_ratio | -2.1088 |
| max_drawdown | 0.9302 |
| cagr | -0.6459 |
| net_avg_win | 37.4796 |
| net_avg_loss | -54.5083 |
| avg_hold_time_bars | 14.4513 |
| exposure | 0.5637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
