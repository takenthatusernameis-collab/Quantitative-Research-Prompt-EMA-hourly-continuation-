# EMA Hourly Continuation — SATS/USDT P26_50

**Symbol:** SATS/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 839 |
| net_profit_factor | 0.5119 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.9055 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -6.4544 |
| sortino_ratio | -2.6368 |
| max_drawdown | 0.9595 |
| cagr | -0.7182 |
| net_avg_win | 27.1873 |
| net_avg_loss | -41.8968 |
| avg_hold_time_bars | 3.7831 |
| exposure | 0.1436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
