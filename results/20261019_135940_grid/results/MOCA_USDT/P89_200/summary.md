# EMA Hourly Continuation — MOCA/USDT P89_200

**Symbol:** MOCA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.4930 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.7898 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -4.5091 |
| sortino_ratio | -1.2600 |
| max_drawdown | 0.7597 |
| cagr | -0.4633 |
| net_avg_win | 47.5334 |
| net_avg_loss | -72.8944 |
| avg_hold_time_bars | 10.9583 |
| exposure | 0.1978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
