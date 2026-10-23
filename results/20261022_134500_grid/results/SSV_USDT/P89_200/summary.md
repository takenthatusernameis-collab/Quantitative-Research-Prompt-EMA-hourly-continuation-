# EMA Hourly Continuation — SSV/USDT P89_200

**Symbol:** SSV/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.5743 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.8676 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -3.9205 |
| sortino_ratio | -1.1506 |
| max_drawdown | 0.7583 |
| cagr | -0.4211 |
| net_avg_win | 51.7549 |
| net_avg_loss | -73.5296 |
| avg_hold_time_bars | 10.0069 |
| exposure | 0.1965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
