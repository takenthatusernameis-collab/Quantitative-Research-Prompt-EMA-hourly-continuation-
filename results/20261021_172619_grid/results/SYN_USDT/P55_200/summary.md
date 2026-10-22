# EMA Hourly Continuation — SYN/USDT P55_200

**Symbol:** SYN/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7625 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9067 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -1.3792 |
| sortino_ratio | -0.3357 |
| max_drawdown | 0.3458 |
| cagr | -0.1439 |
| net_avg_win | 74.1138 |
| net_avg_loss | -89.5228 |
| avg_hold_time_bars | 30.1062 |
| exposure | 0.3996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
