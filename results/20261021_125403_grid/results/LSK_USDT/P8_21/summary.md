# EMA Hourly Continuation — LSK/USDT P8_21

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.7081 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 1.1052 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.7609 |
| sortino_ratio | -1.4640 |
| max_drawdown | 0.8513 |
| cagr | -0.4885 |
| net_avg_win | 54.2783 |
| net_avg_loss | -75.4063 |
| avg_hold_time_bars | 6.3093 |
| exposure | 0.2105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
