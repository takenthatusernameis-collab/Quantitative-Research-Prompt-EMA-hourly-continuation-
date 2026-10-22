# EMA Hourly Continuation — ONDO/USDT P20_21

**Symbol:** ONDO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1188 |
| net_profit_factor | 0.1595 |
| net_win_rate | 0.3030 |
| gross_profit_factor | 0.5276 |
| gross_win_rate | 0.3586 |
| sharpe_ratio | -17.1122 |
| sortino_ratio | -8.8456 |
| max_drawdown | 1.0000 |
| cagr | -0.9934 |
| net_avg_win | 5.2712 |
| net_avg_loss | -14.3691 |
| avg_hold_time_bars | 1.4916 |
| exposure | 0.0805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
