# EMA Hourly Continuation — DAG/USDT P26_34

**Symbol:** DAG/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 117 |
| net_profit_factor | 0.6798 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8530 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -1.3120 |
| sortino_ratio | -0.2017 |
| max_drawdown | 0.2421 |
| cagr | -0.0894 |
| net_avg_win | 82.3670 |
| net_avg_loss | -103.8510 |
| avg_hold_time_bars | 5.6496 |
| exposure | 0.0300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
