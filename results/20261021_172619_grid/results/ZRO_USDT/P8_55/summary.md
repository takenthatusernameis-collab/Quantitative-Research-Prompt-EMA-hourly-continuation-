# EMA Hourly Continuation — ZRO/USDT P8_55

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.9100 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0836 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -0.6828 |
| sortino_ratio | -0.2461 |
| max_drawdown | 0.3369 |
| cagr | -0.1135 |
| net_avg_win | 81.4481 |
| net_avg_loss | -97.8781 |
| avg_hold_time_bars | 16.4811 |
| exposure | 0.4695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
