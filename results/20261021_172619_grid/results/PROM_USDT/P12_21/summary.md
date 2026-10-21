# EMA Hourly Continuation — PROM/USDT P12_21

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.5129 |
| net_win_rate | 0.4283 |
| gross_profit_factor | 0.8261 |
| gross_win_rate | 0.4327 |
| sharpe_ratio | -4.7628 |
| sortino_ratio | -1.4476 |
| max_drawdown | 0.8174 |
| cagr | -0.4905 |
| net_avg_win | 44.2939 |
| net_avg_loss | -64.6888 |
| avg_hold_time_bars | 5.8918 |
| exposure | 0.1213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
