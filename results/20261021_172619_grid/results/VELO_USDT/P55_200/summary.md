# EMA Hourly Continuation — VELO/USDT P55_200

**Symbol:** VELO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.9284 |
| net_win_rate | 0.5228 |
| gross_profit_factor | 1.0807 |
| gross_win_rate | 0.5228 |
| sharpe_ratio | -0.3545 |
| sortino_ratio | -0.0926 |
| max_drawdown | 0.2112 |
| cagr | -0.0461 |
| net_avg_win | 84.2366 |
| net_avg_loss | -99.4027 |
| avg_hold_time_bars | 22.4833 |
| exposure | 0.3362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
