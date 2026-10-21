# EMA Hourly Continuation — PHA/USDT P26_55

**Symbol:** PHA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.7620 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9844 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.8213 |
| sortino_ratio | -0.5535 |
| max_drawdown | 0.4753 |
| cagr | -0.2243 |
| net_avg_win | 67.6919 |
| net_avg_loss | -87.2717 |
| avg_hold_time_bars | 6.6511 |
| exposure | 0.1360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
