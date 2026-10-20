# EMA Hourly Continuation — PUFFER/USDT P8_100

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.8192 |
| net_win_rate | 0.5177 |
| gross_profit_factor | 1.0894 |
| gross_win_rate | 0.5236 |
| sharpe_ratio | -1.5010 |
| sortino_ratio | -0.5371 |
| max_drawdown | 0.4467 |
| cagr | -0.2249 |
| net_avg_win | 69.2386 |
| net_avg_loss | -90.7269 |
| avg_hold_time_bars | 23.1496 |
| exposure | 0.6655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
