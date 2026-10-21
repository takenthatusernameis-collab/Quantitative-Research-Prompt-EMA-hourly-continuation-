# EMA Hourly Continuation — EDU/USDT P89_100

**Symbol:** EDU/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 194 |
| net_profit_factor | 0.5629 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.8151 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -2.4985 |
| sortino_ratio | -0.4961 |
| max_drawdown | 0.4595 |
| cagr | -0.2051 |
| net_avg_win | 65.0806 |
| net_avg_loss | -93.9977 |
| avg_hold_time_bars | 5.3918 |
| exposure | 0.0473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
