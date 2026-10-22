# EMA Hourly Continuation — CFX/USDT P50_55

**Symbol:** CFX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 842 |
| net_profit_factor | 0.1812 |
| net_win_rate | 0.3219 |
| gross_profit_factor | 0.6300 |
| gross_win_rate | 0.3705 |
| sharpe_ratio | -13.4334 |
| sortino_ratio | -5.7624 |
| max_drawdown | 0.9996 |
| cagr | -0.9578 |
| net_avg_win | 8.1630 |
| net_avg_loss | -21.3811 |
| avg_hold_time_bars | 1.8563 |
| exposure | 0.0710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
