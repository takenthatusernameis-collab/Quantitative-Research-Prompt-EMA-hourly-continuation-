# EMA Hourly Continuation — KSM/USDT P100_200

**Symbol:** KSM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7464 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 0.9942 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -1.4971 |
| sortino_ratio | -0.3624 |
| max_drawdown | 0.3933 |
| cagr | -0.1533 |
| net_avg_win | 70.3071 |
| net_avg_loss | -94.8627 |
| avg_hold_time_bars | 11.6246 |
| exposure | 0.1506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
