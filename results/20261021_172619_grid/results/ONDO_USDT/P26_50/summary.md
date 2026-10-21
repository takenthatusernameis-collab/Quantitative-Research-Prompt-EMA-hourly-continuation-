# EMA Hourly Continuation — ONDO/USDT P26_50

**Symbol:** ONDO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.8057 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0520 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.2601 |
| sortino_ratio | -0.3247 |
| max_drawdown | 0.3734 |
| cagr | -0.1386 |
| net_avg_win | 79.0064 |
| net_avg_loss | -102.4308 |
| avg_hold_time_bars | 7.3738 |
| exposure | 0.1076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
