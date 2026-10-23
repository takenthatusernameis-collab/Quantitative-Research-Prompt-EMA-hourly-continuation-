# EMA Hourly Continuation — DAG/USDT P20_50

**Symbol:** DAG/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1038 |
| net_profit_factor | 0.3966 |
| net_win_rate | 0.3988 |
| gross_profit_factor | 0.6544 |
| gross_win_rate | 0.4123 |
| sharpe_ratio | -9.3583 |
| sortino_ratio | -4.2235 |
| max_drawdown | 0.9956 |
| cagr | -0.8840 |
| net_avg_win | 15.8049 |
| net_avg_loss | -26.4399 |
| avg_hold_time_bars | 3.9990 |
| exposure | 0.1887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
