# EMA Hourly Continuation — DAG/USDT P20_55

**Symbol:** DAG/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1010 |
| net_profit_factor | 0.3798 |
| net_win_rate | 0.3950 |
| gross_profit_factor | 0.6181 |
| gross_win_rate | 0.4040 |
| sharpe_ratio | -9.3129 |
| sortino_ratio | -4.1337 |
| max_drawdown | 0.9954 |
| cagr | -0.8808 |
| net_avg_win | 15.2716 |
| net_avg_loss | -26.2611 |
| avg_hold_time_bars | 4.4356 |
| exposure | 0.2036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
