# EMA Hourly Continuation — FLUX/USDT P50_100

**Symbol:** FLUX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.8248 |
| net_win_rate | 0.5237 |
| gross_profit_factor | 1.0896 |
| gross_win_rate | 0.5237 |
| sharpe_ratio | -1.1316 |
| sortino_ratio | -0.3179 |
| max_drawdown | 0.3544 |
| cagr | -0.1374 |
| net_avg_win | 73.3616 |
| net_avg_loss | -97.7917 |
| avg_hold_time_bars | 9.3184 |
| exposure | 0.1610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
