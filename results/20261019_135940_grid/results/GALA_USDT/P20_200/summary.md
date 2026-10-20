# EMA Hourly Continuation — GALA/USDT P20_200

**Symbol:** GALA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.8914 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -2.1413 |
| sortino_ratio | -0.5453 |
| max_drawdown | 0.4837 |
| cagr | -0.2289 |
| net_avg_win | 60.2601 |
| net_avg_loss | -83.3597 |
| avg_hold_time_bars | 45.1006 |
| exposure | 0.6724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
