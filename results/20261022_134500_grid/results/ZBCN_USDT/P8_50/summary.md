# EMA Hourly Continuation — ZBCN/USDT P8_50

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1343 |
| net_profit_factor | 0.6110 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9114 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -5.2925 |
| sortino_ratio | -2.7526 |
| max_drawdown | 0.9628 |
| cagr | -0.7334 |
| net_avg_win | 23.2713 |
| net_avg_loss | -35.6196 |
| avg_hold_time_bars | 6.5793 |
| exposure | 0.4088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
