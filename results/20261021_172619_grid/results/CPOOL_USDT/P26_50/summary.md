# EMA Hourly Continuation — CPOOL/USDT P26_50

**Symbol:** CPOOL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.7468 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9431 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -1.6190 |
| sortino_ratio | -0.4401 |
| max_drawdown | 0.4400 |
| cagr | -0.1835 |
| net_avg_win | 66.1190 |
| net_avg_loss | -86.1190 |
| avg_hold_time_bars | 5.9335 |
| exposure | 0.0974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
