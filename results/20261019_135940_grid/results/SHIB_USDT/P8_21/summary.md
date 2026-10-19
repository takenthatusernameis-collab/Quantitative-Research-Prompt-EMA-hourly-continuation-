# EMA Hourly Continuation — SHIB/USDT P8_21

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1677 |
| net_profit_factor | 0.3332 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 0.7980 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -13.2701 |
| sortino_ratio | -7.6976 |
| max_drawdown | 1.0000 |
| cagr | -0.9815 |
| net_avg_win | 6.9784 |
| net_avg_loss | -15.6047 |
| avg_hold_time_bars | 2.7728 |
| exposure | 0.2114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
