# EMA Hourly Continuation — ROSE/USDT P26_89

**Symbol:** ROSE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 737 |
| net_profit_factor | 0.6774 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9766 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -3.8860 |
| sortino_ratio | -1.4932 |
| max_drawdown | 0.8400 |
| cagr | -0.5052 |
| net_avg_win | 49.3280 |
| net_avg_loss | -66.9387 |
| avg_hold_time_bars | 9.7408 |
| exposure | 0.3263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
