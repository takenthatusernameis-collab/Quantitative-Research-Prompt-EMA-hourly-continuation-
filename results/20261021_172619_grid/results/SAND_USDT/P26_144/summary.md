# EMA Hourly Continuation — SAND/USDT P26_144

**Symbol:** SAND/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.6771 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8392 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -2.3187 |
| sortino_ratio | -0.6076 |
| max_drawdown | 0.5228 |
| cagr | -0.2443 |
| net_avg_win | 68.3246 |
| net_avg_loss | -84.0903 |
| avg_hold_time_bars | 29.7566 |
| exposure | 0.4612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
