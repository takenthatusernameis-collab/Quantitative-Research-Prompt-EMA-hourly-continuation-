# EMA Hourly Continuation — EWT/USDT P50_200

**Symbol:** EWT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.7630 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9097 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -1.5086 |
| sortino_ratio | -0.3687 |
| max_drawdown | 0.4420 |
| cagr | -0.1571 |
| net_avg_win | 80.2454 |
| net_avg_loss | -94.9936 |
| avg_hold_time_bars | 23.5424 |
| exposure | 0.3157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
