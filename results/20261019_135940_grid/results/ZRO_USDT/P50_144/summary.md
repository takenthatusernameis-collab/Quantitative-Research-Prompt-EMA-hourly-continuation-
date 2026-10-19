# EMA Hourly Continuation — ZRO/USDT P50_144

**Symbol:** ZRO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.6481 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.8998 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -3.0453 |
| sortino_ratio | -0.9644 |
| max_drawdown | 0.6583 |
| cagr | -0.3679 |
| net_avg_win | 54.4993 |
| net_avg_loss | -75.5793 |
| avg_hold_time_bars | 10.7399 |
| exposure | 0.2465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
