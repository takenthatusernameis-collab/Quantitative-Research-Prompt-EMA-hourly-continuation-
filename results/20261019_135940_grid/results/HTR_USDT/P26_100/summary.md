# EMA Hourly Continuation — HTR/USDT P26_100

**Symbol:** HTR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.5351 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.7871 |
| gross_win_rate | 0.4385 |
| sharpe_ratio | -5.9363 |
| sortino_ratio | -2.2489 |
| max_drawdown | 0.9379 |
| cagr | -0.6665 |
| net_avg_win | 34.6654 |
| net_avg_loss | -47.8541 |
| avg_hold_time_bars | 10.2172 |
| exposure | 0.3400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
