# EMA Hourly Continuation — DAG/USDT P50_55

**Symbol:** DAG/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 86 |
| net_profit_factor | 0.6380 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.8575 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -1.2602 |
| sortino_ratio | -0.1664 |
| max_drawdown | 0.1740 |
| cagr | -0.0733 |
| net_avg_win | 76.6827 |
| net_avg_loss | -104.5081 |
| avg_hold_time_bars | 4.6628 |
| exposure | 0.0182 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
