# EMA Hourly Continuation — OP/USDT P20_34

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.6358 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.8773 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -2.5219 |
| sortino_ratio | -0.6459 |
| max_drawdown | 0.5278 |
| cagr | -0.2559 |
| net_avg_win | 60.9813 |
| net_avg_loss | -84.1297 |
| avg_hold_time_bars | 4.7601 |
| exposure | 0.0695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
