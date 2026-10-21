# EMA Hourly Continuation — IOTX/USDT P8_50

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.8232 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0647 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -1.6044 |
| sortino_ratio | -0.5953 |
| max_drawdown | 0.5243 |
| cagr | -0.2404 |
| net_avg_win | 67.5221 |
| net_avg_loss | -87.8977 |
| avg_hold_time_bars | 15.0812 |
| exposure | 0.4559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
