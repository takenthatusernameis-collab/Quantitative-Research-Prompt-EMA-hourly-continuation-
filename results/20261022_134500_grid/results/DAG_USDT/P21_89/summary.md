# EMA Hourly Continuation — DAG/USDT P21_89

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 814 |
| net_profit_factor | 0.4831 |
| net_win_rate | 0.4189 |
| gross_profit_factor | 0.7541 |
| gross_win_rate | 0.4287 |
| sharpe_ratio | -6.6736 |
| sortino_ratio | -2.6526 |
| max_drawdown | 0.9654 |
| cagr | -0.7348 |
| net_avg_win | 26.4313 |
| net_avg_loss | -39.4423 |
| avg_hold_time_bars | 8.8428 |
| exposure | 0.3272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
