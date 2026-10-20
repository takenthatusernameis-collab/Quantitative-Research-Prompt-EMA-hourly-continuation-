# EMA Hourly Continuation — AEVO/USDT P20_200

**Symbol:** AEVO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.8552 |
| net_win_rate | 0.5288 |
| gross_profit_factor | 1.1396 |
| gross_win_rate | 0.5321 |
| sharpe_ratio | -0.8662 |
| sortino_ratio | -0.2166 |
| max_drawdown | 0.3107 |
| cagr | -0.0996 |
| net_avg_win | 83.2285 |
| net_avg_loss | -109.2410 |
| avg_hold_time_bars | 48.8494 |
| exposure | 0.6897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
