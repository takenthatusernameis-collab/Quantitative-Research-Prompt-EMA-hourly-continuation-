# EMA Hourly Continuation — DAG/USDT P21_89

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.7879 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9407 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -1.4954 |
| sortino_ratio | -0.4426 |
| max_drawdown | 0.4370 |
| cagr | -0.1853 |
| net_avg_win | 71.1411 |
| net_avg_loss | -86.1932 |
| avg_hold_time_bars | 14.8814 |
| exposure | 0.2909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
