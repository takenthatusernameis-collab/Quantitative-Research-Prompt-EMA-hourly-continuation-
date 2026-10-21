# EMA Hourly Continuation — QNT/USDT P8_12

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.7172 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0877 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -1.7161 |
| sortino_ratio | -0.3834 |
| max_drawdown | 0.3926 |
| cagr | -0.1617 |
| net_avg_win | 73.2081 |
| net_avg_loss | -109.1115 |
| avg_hold_time_bars | 4.9958 |
| exposure | 0.0545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
