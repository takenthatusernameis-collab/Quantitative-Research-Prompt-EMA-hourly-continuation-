# EMA Hourly Continuation — DAG/USDT P12_55

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1085 |
| net_profit_factor | 0.4573 |
| net_win_rate | 0.4258 |
| gross_profit_factor | 0.7097 |
| gross_win_rate | 0.4350 |
| sharpe_ratio | -7.7490 |
| sortino_ratio | -3.5727 |
| max_drawdown | 0.9889 |
| cagr | -0.8299 |
| net_avg_win | 18.0270 |
| net_avg_loss | -29.2319 |
| avg_hold_time_bars | 6.7650 |
| exposure | 0.3336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
