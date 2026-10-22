# EMA Hourly Continuation — BLUR/USDT P8_50

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.8375 |
| net_win_rate | 0.5185 |
| gross_profit_factor | 1.0623 |
| gross_win_rate | 0.5185 |
| sharpe_ratio | -1.4212 |
| sortino_ratio | -0.5403 |
| max_drawdown | 0.5107 |
| cagr | -0.2225 |
| net_avg_win | 66.5383 |
| net_avg_loss | -85.5627 |
| avg_hold_time_bars | 14.6524 |
| exposure | 0.4655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
