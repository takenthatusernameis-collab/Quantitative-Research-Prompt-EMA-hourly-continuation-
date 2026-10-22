# EMA Hourly Continuation — MOODENG/USDT P12_20

**Symbol:** MOODENG/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.7107 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9754 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -1.9967 |
| sortino_ratio | -0.5162 |
| max_drawdown | 0.4354 |
| cagr | -0.2112 |
| net_avg_win | 72.0316 |
| net_avg_loss | -98.3719 |
| avg_hold_time_bars | 5.2015 |
| exposure | 0.0771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
