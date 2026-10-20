# EMA Hourly Continuation — DAG/USDT P20_144

**Symbol:** DAG/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.5775 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.7921 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -4.1399 |
| sortino_ratio | -1.4475 |
| max_drawdown | 0.8324 |
| cagr | -0.5022 |
| net_avg_win | 40.6396 |
| net_avg_loss | -56.7038 |
| avg_hold_time_bars | 16.5088 |
| exposure | 0.4675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
