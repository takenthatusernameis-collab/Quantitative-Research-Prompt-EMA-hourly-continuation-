# EMA Hourly Continuation — OSMO/USDT P26_89

**Symbol:** OSMO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.6636 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8650 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -3.2052 |
| sortino_ratio | -1.0062 |
| max_drawdown | 0.6948 |
| cagr | -0.3705 |
| net_avg_win | 61.6151 |
| net_avg_loss | -76.2229 |
| avg_hold_time_bars | 13.9324 |
| exposure | 0.3090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
