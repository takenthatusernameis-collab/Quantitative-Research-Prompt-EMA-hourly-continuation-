# EMA Hourly Continuation — DASH/USDT P26_200

**Symbol:** DASH/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.4776 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.8193 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -4.3190 |
| sortino_ratio | -1.2253 |
| max_drawdown | 0.7970 |
| cagr | -0.4525 |
| net_avg_win | 39.6061 |
| net_avg_loss | -64.3380 |
| avg_hold_time_bars | 30.2524 |
| exposure | 0.5665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
