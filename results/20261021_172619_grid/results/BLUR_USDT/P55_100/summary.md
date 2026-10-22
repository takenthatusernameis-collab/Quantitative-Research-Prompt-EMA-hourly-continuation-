# EMA Hourly Continuation — BLUR/USDT P55_100

**Symbol:** BLUR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.8269 |
| net_win_rate | 0.5237 |
| gross_profit_factor | 1.0983 |
| gross_win_rate | 0.5237 |
| sharpe_ratio | -1.1498 |
| sortino_ratio | -0.3134 |
| max_drawdown | 0.3975 |
| cagr | -0.1350 |
| net_avg_win | 77.8548 |
| net_avg_loss | -103.5098 |
| avg_hold_time_bars | 7.8942 |
| exposure | 0.1282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
