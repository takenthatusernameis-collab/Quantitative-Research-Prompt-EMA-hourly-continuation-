# EMA Hourly Continuation — GRT/USDT P26_200

**Symbol:** GRT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.9776 |
| net_win_rate | 0.5396 |
| gross_profit_factor | 1.1516 |
| gross_win_rate | 0.5396 |
| sharpe_ratio | -0.0639 |
| sortino_ratio | -0.0150 |
| max_drawdown | 0.1610 |
| cagr | -0.0117 |
| net_avg_win | 89.5928 |
| net_avg_loss | -107.4213 |
| avg_hold_time_bars | 50.2453 |
| exposure | 0.6025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
