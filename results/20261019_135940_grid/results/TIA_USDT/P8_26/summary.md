# EMA Hourly Continuation — TIA/USDT P8_26

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1591 |
| net_profit_factor | 0.5649 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.9596 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -8.8415 |
| sortino_ratio | -4.9649 |
| max_drawdown | 0.9978 |
| cagr | -0.9112 |
| net_avg_win | 18.0385 |
| net_avg_loss | -26.2644 |
| avg_hold_time_bars | 3.6342 |
| exposure | 0.2628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
