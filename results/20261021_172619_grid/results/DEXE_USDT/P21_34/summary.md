# EMA Hourly Continuation — DEXE/USDT P21_34

**Symbol:** DEXE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.6702 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9782 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.0746 |
| sortino_ratio | -0.5253 |
| max_drawdown | 0.4765 |
| cagr | -0.2140 |
| net_avg_win | 59.4959 |
| net_avg_loss | -88.2070 |
| avg_hold_time_bars | 11.4823 |
| exposure | 0.1623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
