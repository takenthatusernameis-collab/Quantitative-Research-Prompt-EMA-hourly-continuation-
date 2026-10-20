# EMA Hourly Continuation — CKB/USDT P8_200

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6315 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.8916 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -2.8182 |
| sortino_ratio | -0.7637 |
| max_drawdown | 0.6167 |
| cagr | -0.3086 |
| net_avg_win | 59.1533 |
| net_avg_loss | -81.5576 |
| avg_hold_time_bars | 47.3963 |
| exposure | 0.8100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
