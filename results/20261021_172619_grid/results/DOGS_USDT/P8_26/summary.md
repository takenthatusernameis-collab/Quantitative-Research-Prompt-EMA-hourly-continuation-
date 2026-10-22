# EMA Hourly Continuation — DOGS/USDT P8_26

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.8834 |
| net_win_rate | 0.5300 |
| gross_profit_factor | 1.1133 |
| gross_win_rate | 0.5300 |
| sharpe_ratio | -0.8320 |
| sortino_ratio | -0.2802 |
| max_drawdown | 0.3617 |
| cagr | -0.1247 |
| net_avg_win | 76.4421 |
| net_avg_loss | -97.5932 |
| avg_hold_time_bars | 7.7017 |
| exposure | 0.1904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
