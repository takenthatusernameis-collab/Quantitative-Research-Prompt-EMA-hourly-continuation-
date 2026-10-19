# EMA Hourly Continuation — STRK/USDT P50_100

**Symbol:** STRK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.6119 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9714 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -4.0599 |
| sortino_ratio | -1.4730 |
| max_drawdown | 0.8348 |
| cagr | -0.5030 |
| net_avg_win | 41.0109 |
| net_avg_loss | -63.4332 |
| avg_hold_time_bars | 5.0902 |
| exposure | 0.1513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
