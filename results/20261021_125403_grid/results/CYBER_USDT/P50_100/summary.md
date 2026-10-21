# EMA Hourly Continuation — CYBER/USDT P50_100

**Symbol:** CYBER/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.7900 |
| net_win_rate | 0.5270 |
| gross_profit_factor | 1.0794 |
| gross_win_rate | 0.5270 |
| sharpe_ratio | -1.3771 |
| sortino_ratio | -0.4184 |
| max_drawdown | 0.4374 |
| cagr | -0.1752 |
| net_avg_win | 61.6603 |
| net_avg_loss | -86.9658 |
| avg_hold_time_bars | 7.9212 |
| exposure | 0.1599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
