# EMA Hourly Continuation — BLUR/USDT P55_144

**Symbol:** BLUR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.7359 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.1117 |
| gross_win_rate | 0.5240 |
| sharpe_ratio | -2.0786 |
| sortino_ratio | -0.6285 |
| max_drawdown | 0.5772 |
| cagr | -0.2582 |
| net_avg_win | 63.0332 |
| net_avg_loss | -89.4779 |
| avg_hold_time_bars | 13.1856 |
| exposure | 0.2733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
