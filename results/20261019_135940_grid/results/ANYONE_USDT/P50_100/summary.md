# EMA Hourly Continuation — ANYONE/USDT P50_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.5230 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.7701 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -4.5873 |
| sortino_ratio | -1.5682 |
| max_drawdown | 0.8247 |
| cagr | -0.5288 |
| net_avg_win | 38.2885 |
| net_avg_loss | -56.9188 |
| avg_hold_time_bars | 6.0150 |
| exposure | 0.1626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
