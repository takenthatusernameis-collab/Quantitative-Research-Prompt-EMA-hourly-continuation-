# EMA Hourly Continuation — LUNA/USDT P26_50

**Symbol:** LUNA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7597 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0381 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -1.7130 |
| sortino_ratio | -0.4521 |
| max_drawdown | 0.4461 |
| cagr | -0.1870 |
| net_avg_win | 75.3774 |
| net_avg_loss | -101.0076 |
| avg_hold_time_bars | 6.2997 |
| exposure | 0.0965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
