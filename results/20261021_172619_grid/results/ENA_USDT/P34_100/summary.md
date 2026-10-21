# EMA Hourly Continuation — ENA/USDT P34_100

**Symbol:** ENA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.9712 |
| net_win_rate | 0.5345 |
| gross_profit_factor | 1.1413 |
| gross_win_rate | 0.5371 |
| sharpe_ratio | -0.1175 |
| sortino_ratio | -0.0336 |
| max_drawdown | 0.2575 |
| cagr | -0.0221 |
| net_avg_win | 87.8813 |
| net_avg_loss | -103.9154 |
| avg_hold_time_bars | 14.0026 |
| exposure | 0.2489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
