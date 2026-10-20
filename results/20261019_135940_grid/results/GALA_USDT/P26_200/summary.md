# EMA Hourly Continuation — GALA/USDT P26_200

**Symbol:** GALA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6649 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9292 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.1545 |
| sortino_ratio | -0.5786 |
| max_drawdown | 0.5214 |
| cagr | -0.2430 |
| net_avg_win | 55.7409 |
| net_avg_loss | -79.8223 |
| avg_hold_time_bars | 34.6267 |
| exposure | 0.5776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
