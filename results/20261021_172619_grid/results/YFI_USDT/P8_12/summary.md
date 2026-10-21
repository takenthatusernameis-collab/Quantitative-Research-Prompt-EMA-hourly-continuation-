# EMA Hourly Continuation — YFI/USDT P8_12

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.4441 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.8163 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -4.8458 |
| sortino_ratio | -1.3827 |
| max_drawdown | 0.7996 |
| cagr | -0.4713 |
| net_avg_win | 36.7108 |
| net_avg_loss | -66.2848 |
| avg_hold_time_bars | 4.6189 |
| exposure | 0.0817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
