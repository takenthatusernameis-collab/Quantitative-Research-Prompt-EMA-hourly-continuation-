# EMA Hourly Continuation — POPCAT/USDT P20_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.7213 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8193 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -1.8927 |
| sortino_ratio | -0.5076 |
| max_drawdown | 0.4271 |
| cagr | -0.2094 |
| net_avg_win | 73.6091 |
| net_avg_loss | -84.5377 |
| avg_hold_time_bars | 34.7508 |
| exposure | 0.5672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
