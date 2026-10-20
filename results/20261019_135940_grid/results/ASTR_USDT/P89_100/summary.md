# EMA Hourly Continuation — ASTR/USDT P89_100

**Symbol:** ASTR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.2133 |
| net_win_rate | 0.3904 |
| gross_profit_factor | 0.6678 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -9.2166 |
| sortino_ratio | -3.1910 |
| max_drawdown | 0.9863 |
| cagr | -0.8157 |
| net_avg_win | 12.2043 |
| net_avg_loss | -36.6445 |
| avg_hold_time_bars | 3.0980 |
| exposure | 0.0786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
