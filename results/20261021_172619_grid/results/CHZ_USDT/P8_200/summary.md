# EMA Hourly Continuation — CHZ/USDT P8_200

**Symbol:** CHZ/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.9348 |
| net_win_rate | 0.5294 |
| gross_profit_factor | 1.1102 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | -0.3075 |
| sortino_ratio | -0.0730 |
| max_drawdown | 0.3290 |
| cagr | -0.0367 |
| net_avg_win | 89.2192 |
| net_avg_loss | -107.3767 |
| avg_hold_time_bars | 65.0441 |
| exposure | 0.8042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
