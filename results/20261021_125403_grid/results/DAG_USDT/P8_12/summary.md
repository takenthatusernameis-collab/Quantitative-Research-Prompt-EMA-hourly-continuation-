# EMA Hourly Continuation — DAG/USDT P8_12

**Symbol:** DAG/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 178 |
| net_profit_factor | 0.5501 |
| net_win_rate | 0.4213 |
| gross_profit_factor | 0.7049 |
| gross_win_rate | 0.4213 |
| sharpe_ratio | -2.3645 |
| sortino_ratio | -0.4460 |
| max_drawdown | 0.4246 |
| cagr | -0.1857 |
| net_avg_win | 65.7050 |
| net_avg_loss | -86.9716 |
| avg_hold_time_bars | 6.1461 |
| exposure | 0.0497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
