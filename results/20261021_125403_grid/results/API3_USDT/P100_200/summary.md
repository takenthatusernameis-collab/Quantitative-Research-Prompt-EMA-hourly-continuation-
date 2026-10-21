# EMA Hourly Continuation — API3/USDT P100_200

**Symbol:** API3/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.7848 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0007 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -1.2769 |
| sortino_ratio | -0.3138 |
| max_drawdown | 0.3726 |
| cagr | -0.1353 |
| net_avg_win | 75.3628 |
| net_avg_loss | -97.3392 |
| avg_hold_time_bars | 12.5272 |
| exposure | 0.1674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
