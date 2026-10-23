# EMA Hourly Continuation — CGPT/USDT P89_100

**Symbol:** CGPT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.2896 |
| net_win_rate | 0.4153 |
| gross_profit_factor | 0.8199 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -8.1347 |
| sortino_ratio | -2.7506 |
| max_drawdown | 0.9735 |
| cagr | -0.7608 |
| net_avg_win | 17.3869 |
| net_avg_loss | -42.6444 |
| avg_hold_time_bars | 1.9107 |
| exposure | 0.0477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
