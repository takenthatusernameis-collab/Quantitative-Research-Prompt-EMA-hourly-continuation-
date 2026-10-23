# EMA Hourly Continuation — SATS/USDT P26_200

**Symbol:** SATS/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.5476 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.7558 |
| gross_win_rate | 0.4316 |
| sharpe_ratio | -3.6613 |
| sortino_ratio | -1.0587 |
| max_drawdown | 0.7216 |
| cagr | -0.3921 |
| net_avg_win | 47.5505 |
| net_avg_loss | -65.3103 |
| avg_hold_time_bars | 25.8561 |
| exposure | 0.4961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
