# EMA Hourly Continuation — ETH/USDT P100_200

**Symbol:** ETH/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.4360 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.8593 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -4.4892 |
| sortino_ratio | -1.2357 |
| max_drawdown | 0.7834 |
| cagr | -0.4493 |
| net_avg_win | 34.4987 |
| net_avg_loss | -67.1556 |
| avg_hold_time_bars | 9.0185 |
| exposure | 0.1554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
