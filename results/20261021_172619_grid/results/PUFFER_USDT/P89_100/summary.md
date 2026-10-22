# EMA Hourly Continuation — PUFFER/USDT P89_100

**Symbol:** PUFFER/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 130 |
| net_profit_factor | 0.6144 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8377 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -1.8236 |
| sortino_ratio | -0.3308 |
| max_drawdown | 0.2713 |
| cagr | -0.1399 |
| net_avg_win | 69.6431 |
| net_avg_loss | -97.1539 |
| avg_hold_time_bars | 6.4000 |
| exposure | 0.0471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
