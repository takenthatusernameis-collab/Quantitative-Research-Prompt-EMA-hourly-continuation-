# EMA Hourly Continuation — DAG/USDT P21_34

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 0.7459 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9723 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.2095 |
| sortino_ratio | -0.2355 |
| max_drawdown | 0.3104 |
| cagr | -0.1032 |
| net_avg_win | 76.3564 |
| net_avg_loss | -101.2611 |
| avg_hold_time_bars | 5.7514 |
| exposure | 0.0484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
