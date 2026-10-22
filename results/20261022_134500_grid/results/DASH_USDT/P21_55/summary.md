# EMA Hourly Continuation — DASH/USDT P21_55

**Symbol:** DASH/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 950 |
| net_profit_factor | 0.4062 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.8998 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -7.7476 |
| sortino_ratio | -3.3486 |
| max_drawdown | 0.9850 |
| cagr | -0.8121 |
| net_avg_win | 16.2336 |
| net_avg_loss | -31.0032 |
| avg_hold_time_bars | 5.4326 |
| exposure | 0.2346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
