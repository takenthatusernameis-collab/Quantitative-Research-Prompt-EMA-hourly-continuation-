# EMA Hourly Continuation — ALGO/USDT P26_50

**Symbol:** ALGO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.7911 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1064 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -1.3400 |
| sortino_ratio | -0.3820 |
| max_drawdown | 0.3772 |
| cagr | -0.1607 |
| net_avg_win | 65.4280 |
| net_avg_loss | -93.0982 |
| avg_hold_time_bars | 5.6350 |
| exposure | 0.0996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
