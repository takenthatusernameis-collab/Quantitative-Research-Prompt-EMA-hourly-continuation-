# EMA Hourly Continuation — DAG/USDT P8_34

**Symbol:** DAG/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1452 |
| net_profit_factor | 0.4367 |
| net_win_rate | 0.3974 |
| gross_profit_factor | 0.7301 |
| gross_win_rate | 0.4063 |
| sharpe_ratio | -11.4123 |
| sortino_ratio | -6.0648 |
| max_drawdown | 0.9996 |
| cagr | -0.9557 |
| net_avg_win | 13.4308 |
| net_avg_loss | -20.2806 |
| avg_hold_time_bars | 4.7314 |
| exposure | 0.3123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
