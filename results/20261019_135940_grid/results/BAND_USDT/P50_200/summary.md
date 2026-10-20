# EMA Hourly Continuation — BAND/USDT P50_200

**Symbol:** BAND/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6704 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9269 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.4017 |
| sortino_ratio | -0.6528 |
| max_drawdown | 0.5625 |
| cagr | -0.2630 |
| net_avg_win | 61.3436 |
| net_avg_loss | -84.3966 |
| avg_hold_time_bars | 23.8949 |
| exposure | 0.4011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
