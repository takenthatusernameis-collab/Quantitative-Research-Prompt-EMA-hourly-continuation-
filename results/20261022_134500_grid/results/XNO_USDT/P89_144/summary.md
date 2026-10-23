# EMA Hourly Continuation — XNO/USDT P89_144

**Symbol:** XNO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.4301 |
| net_win_rate | 0.3906 |
| gross_profit_factor | 0.7741 |
| gross_win_rate | 0.4103 |
| sharpe_ratio | -7.4539 |
| sortino_ratio | -2.7363 |
| max_drawdown | 0.9639 |
| cagr | -0.7334 |
| net_avg_win | 28.0862 |
| net_avg_loss | -41.8637 |
| avg_hold_time_bars | 4.6561 |
| exposure | 0.1403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
