# EMA Hourly Continuation — DEXE/USDT P34_89

**Symbol:** DEXE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.7897 |
| net_win_rate | 0.5108 |
| gross_profit_factor | 1.0224 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -1.2942 |
| sortino_ratio | -0.3572 |
| max_drawdown | 0.3953 |
| cagr | -0.1523 |
| net_avg_win | 67.4573 |
| net_avg_loss | -89.2006 |
| avg_hold_time_bars | 22.9649 |
| exposure | 0.3862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
