# EMA Hourly Continuation — MOODENG/USDT P8_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 213 |
| net_profit_factor | 1.0567 |
| net_win_rate | 0.5587 |
| gross_profit_factor | 1.2608 |
| gross_win_rate | 0.5634 |
| sharpe_ratio | 0.3519 |
| sortino_ratio | 0.0823 |
| max_drawdown | 0.1603 |
| cagr | 0.0311 |
| net_avg_win | 101.9961 |
| net_avg_loss | -122.1917 |
| avg_hold_time_bars | 71.3427 |
| exposure | 0.8408 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
