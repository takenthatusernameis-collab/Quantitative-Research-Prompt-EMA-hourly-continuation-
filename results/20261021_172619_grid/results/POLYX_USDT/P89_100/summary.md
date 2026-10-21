# EMA Hourly Continuation — POLYX/USDT P89_100

**Symbol:** POLYX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.7702 |
| net_win_rate | 0.5489 |
| gross_profit_factor | 1.2473 |
| gross_win_rate | 0.5489 |
| sharpe_ratio | -1.1935 |
| sortino_ratio | -0.2350 |
| max_drawdown | 0.3204 |
| cagr | -0.1009 |
| net_avg_win | 77.8106 |
| net_avg_loss | -122.9330 |
| avg_hold_time_bars | 5.5489 |
| exposure | 0.0464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
