# EMA Hourly Continuation — LINK/USDT P50_89

**Symbol:** LINK/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.4896 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.9454 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -6.0635 |
| sortino_ratio | -2.1357 |
| max_drawdown | 0.9321 |
| cagr | -0.6538 |
| net_avg_win | 30.9834 |
| net_avg_loss | -54.5707 |
| avg_hold_time_bars | 4.8489 |
| exposure | 0.1371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
