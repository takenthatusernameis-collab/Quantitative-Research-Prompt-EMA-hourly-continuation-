# EMA Hourly Continuation — ROSE/USDT P20_200

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7261 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9523 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -1.8241 |
| sortino_ratio | -0.4859 |
| max_drawdown | 0.4574 |
| cagr | -0.2034 |
| net_avg_win | 66.6794 |
| net_avg_loss | -88.2602 |
| avg_hold_time_bars | 43.1870 |
| exposure | 0.6930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
