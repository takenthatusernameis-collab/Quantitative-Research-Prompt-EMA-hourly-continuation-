# EMA Hourly Continuation — VELO/USDT P26_100

**Symbol:** VELO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.7240 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -2.8242 |
| sortino_ratio | -1.0662 |
| max_drawdown | 0.7495 |
| cagr | -0.3946 |
| net_avg_win | 53.5459 |
| net_avg_loss | -72.9188 |
| avg_hold_time_bars | 10.6054 |
| exposure | 0.3408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
