# EMA Hourly Continuation — BAND/USDT P26_89

**Symbol:** BAND/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.7106 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9454 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -2.6465 |
| sortino_ratio | -0.8521 |
| max_drawdown | 0.6415 |
| cagr | -0.3236 |
| net_avg_win | 63.1168 |
| net_avg_loss | -80.8630 |
| avg_hold_time_bars | 13.1895 |
| exposure | 0.3056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
