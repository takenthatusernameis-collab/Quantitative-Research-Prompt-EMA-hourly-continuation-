# EMA Hourly Continuation — ALGO/USDT P8_50

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.8485 |
| net_win_rate | 0.5217 |
| gross_profit_factor | 1.0805 |
| gross_win_rate | 0.5217 |
| sharpe_ratio | -1.2898 |
| sortino_ratio | -0.4888 |
| max_drawdown | 0.4599 |
| cagr | -0.2041 |
| net_avg_win | 67.7018 |
| net_avg_loss | -87.0192 |
| avg_hold_time_bars | 12.8801 |
| exposure | 0.4051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
