# EMA Hourly Continuation — ZBCN/USDT P34_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 768 |
| net_profit_factor | 0.5510 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8097 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -4.9913 |
| sortino_ratio | -1.9680 |
| max_drawdown | 0.9071 |
| cagr | -0.6070 |
| net_avg_win | 32.0251 |
| net_avg_loss | -47.4009 |
| avg_hold_time_bars | 6.4518 |
| exposure | 0.2292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
