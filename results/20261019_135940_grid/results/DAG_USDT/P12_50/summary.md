# EMA Hourly Continuation — DAG/USDT P12_50

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1144 |
| net_profit_factor | 0.4178 |
| net_win_rate | 0.4152 |
| gross_profit_factor | 0.6715 |
| gross_win_rate | 0.4248 |
| sharpe_ratio | -8.7814 |
| sortino_ratio | -4.1455 |
| max_drawdown | 0.9951 |
| cagr | -0.8765 |
| net_avg_win | 15.0295 |
| net_avg_loss | -25.5406 |
| avg_hold_time_bars | 5.8479 |
| exposure | 0.3041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
