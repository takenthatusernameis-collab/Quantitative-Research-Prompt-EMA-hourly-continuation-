# EMA Hourly Continuation — BONK/USDT P8_200

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7338 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0254 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.8996 |
| sortino_ratio | -0.5128 |
| max_drawdown | 0.5177 |
| cagr | -0.2200 |
| net_avg_win | 68.7764 |
| net_avg_loss | -94.2386 |
| avg_hold_time_bars | 47.7197 |
| exposure | 0.8047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
