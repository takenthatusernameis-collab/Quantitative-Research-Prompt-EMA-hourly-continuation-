# EMA Hourly Continuation — ARB/USDT P50_55

**Symbol:** ARB/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 98 |
| net_profit_factor | 0.8341 |
| net_win_rate | 0.5306 |
| gross_profit_factor | 1.1270 |
| gross_win_rate | 0.5306 |
| sharpe_ratio | -0.5483 |
| sortino_ratio | -0.0784 |
| max_drawdown | 0.1465 |
| cagr | -0.0355 |
| net_avg_win | 83.9846 |
| net_avg_loss | -113.8288 |
| avg_hold_time_bars | 5.8163 |
| exposure | 0.0259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
