# EMA Hourly Continuation — CGPT/USDT P12_100

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.6321 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.9503 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -3.7719 |
| sortino_ratio | -1.2907 |
| max_drawdown | 0.8017 |
| cagr | -0.4694 |
| net_avg_win | 48.0128 |
| net_avg_loss | -67.6477 |
| avg_hold_time_bars | 21.2893 |
| exposure | 0.5855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
