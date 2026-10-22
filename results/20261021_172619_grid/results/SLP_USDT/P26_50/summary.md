# EMA Hourly Continuation — SLP/USDT P26_50

**Symbol:** SLP/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.7277 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 1.0182 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -2.5284 |
| sortino_ratio | -0.7782 |
| max_drawdown | 0.6185 |
| cagr | -0.2993 |
| net_avg_win | 69.8477 |
| net_avg_loss | -92.7003 |
| avg_hold_time_bars | 5.5217 |
| exposure | 0.1155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
