# EMA Hourly Continuation — BRETT/USDT P34_200

**Symbol:** BRETT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.6839 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8297 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -2.0127 |
| sortino_ratio | -0.5007 |
| max_drawdown | 0.4291 |
| cagr | -0.2082 |
| net_avg_win | 68.6555 |
| net_avg_loss | -84.6024 |
| avg_hold_time_bars | 38.8430 |
| exposure | 0.5476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
