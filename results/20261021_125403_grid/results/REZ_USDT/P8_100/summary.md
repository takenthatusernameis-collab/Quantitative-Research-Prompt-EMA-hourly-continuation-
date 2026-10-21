# EMA Hourly Continuation — REZ/USDT P8_100

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.9654 |
| net_win_rate | 0.5311 |
| gross_profit_factor | 1.1216 |
| gross_win_rate | 0.5311 |
| sharpe_ratio | -0.1962 |
| sortino_ratio | -0.0626 |
| max_drawdown | 0.3261 |
| cagr | -0.0365 |
| net_avg_win | 95.6597 |
| net_avg_loss | -112.2457 |
| avg_hold_time_bars | 29.0394 |
| exposure | 0.6458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
