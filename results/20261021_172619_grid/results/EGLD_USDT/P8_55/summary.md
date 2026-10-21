# EMA Hourly Continuation — EGLD/USDT P8_55

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.8390 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0844 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.6545 |
| sortino_ratio | -0.6244 |
| max_drawdown | 0.5979 |
| cagr | -0.2511 |
| net_avg_win | 75.7454 |
| net_avg_loss | -95.9621 |
| avg_hold_time_bars | 14.7968 |
| exposure | 0.4634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
