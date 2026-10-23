# EMA Hourly Continuation — DYDX/USDT P89_200

**Symbol:** DYDX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.6292 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9046 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -2.8447 |
| sortino_ratio | -0.7985 |
| max_drawdown | 0.6217 |
| cagr | -0.3113 |
| net_avg_win | 56.0708 |
| net_avg_loss | -78.8357 |
| avg_hold_time_bars | 10.7372 |
| exposure | 0.1913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
