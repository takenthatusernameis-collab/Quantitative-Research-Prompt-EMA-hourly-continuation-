# EMA Hourly Continuation — MAGIC/USDT P8_26

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 810 |
| net_profit_factor | 0.7148 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9812 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -3.7237 |
| sortino_ratio | -1.5157 |
| max_drawdown | 0.8351 |
| cagr | -0.5012 |
| net_avg_win | 53.0655 |
| net_avg_loss | -68.9329 |
| avg_hold_time_bars | 7.0988 |
| exposure | 0.2614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
