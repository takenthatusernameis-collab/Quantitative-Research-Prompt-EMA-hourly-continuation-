# EMA Hourly Continuation — GRAM/USDT P8_50

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1173 |
| net_profit_factor | 0.4452 |
| net_win_rate | 0.4314 |
| gross_profit_factor | 0.8950 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -9.3341 |
| sortino_ratio | -4.4789 |
| max_drawdown | 0.9969 |
| cagr | -0.8978 |
| net_avg_win | 15.8040 |
| net_avg_loss | -26.9330 |
| avg_hold_time_bars | 8.4970 |
| exposure | 0.4530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
