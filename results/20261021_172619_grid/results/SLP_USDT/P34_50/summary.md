# EMA Hourly Continuation — SLP/USDT P34_50

**Symbol:** SLP/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.6509 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.9371 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -2.7662 |
| sortino_ratio | -0.7013 |
| max_drawdown | 0.5876 |
| cagr | -0.2748 |
| net_avg_win | 70.7099 |
| net_avg_loss | -94.9791 |
| avg_hold_time_bars | 4.0895 |
| exposure | 0.0582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
