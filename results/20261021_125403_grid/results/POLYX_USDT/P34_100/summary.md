# EMA Hourly Continuation — POLYX/USDT P34_100

**Symbol:** POLYX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.7933 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.0500 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -1.7859 |
| sortino_ratio | -0.5492 |
| max_drawdown | 0.5177 |
| cagr | -0.2236 |
| net_avg_win | 77.4490 |
| net_avg_loss | -99.7749 |
| avg_hold_time_bars | 13.7484 |
| exposure | 0.2881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
