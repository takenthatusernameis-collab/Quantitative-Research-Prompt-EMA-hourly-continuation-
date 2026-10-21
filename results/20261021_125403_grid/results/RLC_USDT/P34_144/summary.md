# EMA Hourly Continuation — RLC/USDT P34_144

**Symbol:** RLC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7658 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9617 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.6636 |
| sortino_ratio | -0.4754 |
| max_drawdown | 0.4598 |
| cagr | -0.1972 |
| net_avg_win | 70.3691 |
| net_avg_loss | -89.1712 |
| avg_hold_time_bars | 21.6175 |
| exposure | 0.3930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
