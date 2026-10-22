# EMA Hourly Continuation — TRAC/USDT P26_50

**Symbol:** TRAC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 820 |
| net_profit_factor | 0.4560 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8578 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -6.7548 |
| sortino_ratio | -2.7311 |
| max_drawdown | 0.9658 |
| cagr | -0.7354 |
| net_avg_win | 21.9100 |
| net_avg_loss | -39.3124 |
| avg_hold_time_bars | 5.1963 |
| exposure | 0.1937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
