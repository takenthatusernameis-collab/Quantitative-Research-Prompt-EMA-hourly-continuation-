# EMA Hourly Continuation — DAG/USDT P20_200

**Symbol:** DAG/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6761 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.8936 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -2.3572 |
| sortino_ratio | -0.6932 |
| max_drawdown | 0.5820 |
| cagr | -0.2804 |
| net_avg_win | 56.6911 |
| net_avg_loss | -76.1320 |
| avg_hold_time_bars | 29.4805 |
| exposure | 0.5829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
