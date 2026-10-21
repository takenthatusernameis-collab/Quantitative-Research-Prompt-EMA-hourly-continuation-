# EMA Hourly Continuation — JUP/USDT P89_144

**Symbol:** JUP/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.6738 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8568 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -2.0753 |
| sortino_ratio | -0.4668 |
| max_drawdown | 0.4531 |
| cagr | -0.1928 |
| net_avg_win | 75.3778 |
| net_avg_loss | -93.7722 |
| avg_hold_time_bars | 7.8360 |
| exposure | 0.0890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
