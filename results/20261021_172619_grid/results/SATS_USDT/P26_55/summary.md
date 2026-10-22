# EMA Hourly Continuation — SATS/USDT P26_55

**Symbol:** SATS/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.5697 |
| net_win_rate | 0.4261 |
| gross_profit_factor | 0.7659 |
| gross_win_rate | 0.4283 |
| sharpe_ratio | -4.0003 |
| sortino_ratio | -1.2211 |
| max_drawdown | 0.7669 |
| cagr | -0.4344 |
| net_avg_win | 50.7379 |
| net_avg_loss | -66.1278 |
| avg_hold_time_bars | 6.6210 |
| exposure | 0.1399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
