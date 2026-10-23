# EMA Hourly Continuation — DOGS/USDT P26_100

**Symbol:** DOGS/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.6792 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 0.9891 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -3.0364 |
| sortino_ratio | -1.1225 |
| max_drawdown | 0.6818 |
| cagr | -0.4108 |
| net_avg_win | 48.9490 |
| net_avg_loss | -72.8077 |
| avg_hold_time_bars | 11.6513 |
| exposure | 0.3616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
