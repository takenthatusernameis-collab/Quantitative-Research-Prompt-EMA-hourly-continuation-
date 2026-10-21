# EMA Hourly Continuation — CGPT/USDT P89_100

**Symbol:** CGPT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 97 |
| net_profit_factor | 0.8056 |
| net_win_rate | 0.5361 |
| gross_profit_factor | 1.1426 |
| gross_win_rate | 0.5361 |
| sharpe_ratio | -0.6285 |
| sortino_ratio | -0.0894 |
| max_drawdown | 0.1216 |
| cagr | -0.0405 |
| net_avg_win | 78.5236 |
| net_avg_loss | -112.6317 |
| avg_hold_time_bars | 4.2371 |
| exposure | 0.0187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
