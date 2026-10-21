# EMA Hourly Continuation — RIO/USDT P8_200

**Symbol:** RIO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.9669 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0702 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -0.1513 |
| sortino_ratio | -0.0405 |
| max_drawdown | 0.2086 |
| cagr | -0.0244 |
| net_avg_win | 97.7855 |
| net_avg_loss | -108.4447 |
| avg_hold_time_bars | 47.7355 |
| exposure | 0.7539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
