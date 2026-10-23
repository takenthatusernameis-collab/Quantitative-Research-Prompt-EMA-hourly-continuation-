# EMA Hourly Continuation — TAIKO/USDT P26_50

**Symbol:** TAIKO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 831 |
| net_profit_factor | 0.4787 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.8807 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -7.5733 |
| sortino_ratio | -3.1728 |
| max_drawdown | 0.9767 |
| cagr | -0.7921 |
| net_avg_win | 23.8338 |
| net_avg_loss | -41.1479 |
| avg_hold_time_bars | 4.3069 |
| exposure | 0.1719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
