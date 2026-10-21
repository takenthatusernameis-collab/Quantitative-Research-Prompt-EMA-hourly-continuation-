# EMA Hourly Continuation — SAFE/USDT P26_100

**Symbol:** SAFE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.8899 |
| net_win_rate | 0.5261 |
| gross_profit_factor | 1.1072 |
| gross_win_rate | 0.5261 |
| sharpe_ratio | -0.7804 |
| sortino_ratio | -0.2368 |
| max_drawdown | 0.3400 |
| cagr | -0.1070 |
| net_avg_win | 85.6583 |
| net_avg_loss | -106.8437 |
| avg_hold_time_bars | 17.3311 |
| exposure | 0.3500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
