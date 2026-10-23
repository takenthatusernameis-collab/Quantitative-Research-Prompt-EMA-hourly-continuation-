# EMA Hourly Continuation — FIDA/USDT P21_200

**Symbol:** FIDA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.5762 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.8249 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -3.2426 |
| sortino_ratio | -0.8978 |
| max_drawdown | 0.6732 |
| cagr | -0.3485 |
| net_avg_win | 51.3398 |
| net_avg_loss | -72.1859 |
| avg_hold_time_bars | 36.2199 |
| exposure | 0.6408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
