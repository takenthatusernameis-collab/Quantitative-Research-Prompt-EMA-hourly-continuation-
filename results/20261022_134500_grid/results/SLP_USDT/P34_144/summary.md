# EMA Hourly Continuation — SLP/USDT P34_144

**Symbol:** SLP/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.6369 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.9218 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -3.8309 |
| sortino_ratio | -1.2986 |
| max_drawdown | 0.7950 |
| cagr | -0.4580 |
| net_avg_win | 51.9656 |
| net_avg_loss | -70.6637 |
| avg_hold_time_bars | 16.0123 |
| exposure | 0.4156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
