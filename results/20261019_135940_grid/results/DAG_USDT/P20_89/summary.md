# EMA Hourly Continuation — DAG/USDT P20_89

**Symbol:** DAG/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 811 |
| net_profit_factor | 0.4816 |
| net_win_rate | 0.4192 |
| gross_profit_factor | 0.7466 |
| gross_win_rate | 0.4291 |
| sharpe_ratio | -6.6453 |
| sortino_ratio | -2.6288 |
| max_drawdown | 0.9654 |
| cagr | -0.7337 |
| net_avg_win | 26.3420 |
| net_avg_loss | -39.4818 |
| avg_hold_time_bars | 9.1455 |
| exposure | 0.3371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
