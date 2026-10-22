# EMA Hourly Continuation — DODO/USDT P20_89

**Symbol:** DODO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.8074 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 1.0141 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.7340 |
| sortino_ratio | -0.5516 |
| max_drawdown | 0.5430 |
| cagr | -0.2246 |
| net_avg_win | 80.3957 |
| net_avg_loss | -98.3778 |
| avg_hold_time_bars | 17.1046 |
| exposure | 0.3847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
