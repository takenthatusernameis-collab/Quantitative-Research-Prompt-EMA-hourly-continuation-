# EMA Hourly Continuation — PROM/USDT P55_100

**Symbol:** PROM/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.4116 |
| net_win_rate | 0.4080 |
| gross_profit_factor | 0.8307 |
| gross_win_rate | 0.4422 |
| sharpe_ratio | -7.6455 |
| sortino_ratio | -2.8713 |
| max_drawdown | 0.9740 |
| cagr | -0.7578 |
| net_avg_win | 23.7666 |
| net_avg_loss | -39.7910 |
| avg_hold_time_bars | 5.7461 |
| exposure | 0.1831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
