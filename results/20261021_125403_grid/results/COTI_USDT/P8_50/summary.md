# EMA Hourly Continuation — COTI/USDT P8_50

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.8341 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0199 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.6235 |
| sortino_ratio | -0.6361 |
| max_drawdown | 0.5702 |
| cagr | -0.2560 |
| net_avg_win | 69.9173 |
| net_avg_loss | -85.4051 |
| avg_hold_time_bars | 12.2544 |
| exposure | 0.4161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
