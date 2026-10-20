# EMA Hourly Continuation — DAG/USDT P50_200

**Symbol:** DAG/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.6253 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.8750 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -2.9581 |
| sortino_ratio | -0.8571 |
| max_drawdown | 0.6567 |
| cagr | -0.3418 |
| net_avg_win | 53.4508 |
| net_avg_loss | -75.7765 |
| avg_hold_time_bars | 17.6898 |
| exposure | 0.3474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
