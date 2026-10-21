# EMA Hourly Continuation — AXL/USDT P50_55

**Symbol:** AXL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 198 |
| net_profit_factor | 0.4249 |
| net_win_rate | 0.3687 |
| gross_profit_factor | 0.5928 |
| gross_win_rate | 0.3687 |
| sharpe_ratio | -3.7713 |
| sortino_ratio | -0.7527 |
| max_drawdown | 0.6017 |
| cagr | -0.2963 |
| net_avg_win | 59.5004 |
| net_avg_loss | -81.7757 |
| avg_hold_time_bars | 5.2778 |
| exposure | 0.0473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
