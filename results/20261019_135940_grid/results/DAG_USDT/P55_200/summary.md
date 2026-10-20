# EMA Hourly Continuation — DAG/USDT P55_200

**Symbol:** DAG/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.6020 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8376 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -3.1293 |
| sortino_ratio | -0.9017 |
| max_drawdown | 0.6698 |
| cagr | -0.3520 |
| net_avg_win | 51.4798 |
| net_avg_loss | -72.8146 |
| avg_hold_time_bars | 16.9127 |
| exposure | 0.3260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
