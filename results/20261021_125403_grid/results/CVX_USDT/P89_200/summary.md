# EMA Hourly Continuation — CVX/USDT P89_200

**Symbol:** CVX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.7605 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9395 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.3567 |
| sortino_ratio | -0.3154 |
| max_drawdown | 0.3063 |
| cagr | -0.1355 |
| net_avg_win | 75.3912 |
| net_avg_loss | -94.0344 |
| avg_hold_time_bars | 14.3887 |
| exposure | 0.1733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
