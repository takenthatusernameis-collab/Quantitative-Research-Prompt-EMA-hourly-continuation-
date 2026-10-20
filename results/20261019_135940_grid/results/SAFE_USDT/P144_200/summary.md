# EMA Hourly Continuation — SAFE/USDT P144_200

**Symbol:** SAFE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.3919 |
| net_win_rate | 0.4209 |
| gross_profit_factor | 0.6912 |
| gross_win_rate | 0.4236 |
| sharpe_ratio | -5.1477 |
| sortino_ratio | -1.4122 |
| max_drawdown | 0.8285 |
| cagr | -0.5012 |
| net_avg_win | 33.7942 |
| net_avg_loss | -62.6806 |
| avg_hold_time_bars | 7.2413 |
| exposure | 0.1237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
