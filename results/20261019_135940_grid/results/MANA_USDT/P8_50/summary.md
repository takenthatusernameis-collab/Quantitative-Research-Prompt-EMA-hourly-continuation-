# EMA Hourly Continuation — MANA/USDT P8_50

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1071 |
| net_profit_factor | 0.5725 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.9927 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -7.3056 |
| sortino_ratio | -3.3468 |
| max_drawdown | 0.9849 |
| cagr | -0.8085 |
| net_avg_win | 27.3405 |
| net_avg_loss | -39.0842 |
| avg_hold_time_bars | 9.7003 |
| exposure | 0.4722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
