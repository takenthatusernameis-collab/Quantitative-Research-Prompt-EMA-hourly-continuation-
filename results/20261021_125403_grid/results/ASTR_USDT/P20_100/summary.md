# EMA Hourly Continuation — ASTR/USDT P20_100

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.7956 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0471 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.6241 |
| sortino_ratio | -0.5111 |
| max_drawdown | 0.5046 |
| cagr | -0.2103 |
| net_avg_win | 70.7123 |
| net_avg_loss | -92.6318 |
| avg_hold_time_bars | 20.1426 |
| exposure | 0.4412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
