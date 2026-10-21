# EMA Hourly Continuation — DUSK/USDT P26_100

**Symbol:** DUSK/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.8172 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 0.9861 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -1.3731 |
| sortino_ratio | -0.4240 |
| max_drawdown | 0.4554 |
| cagr | -0.1788 |
| net_avg_win | 75.5103 |
| net_avg_loss | -90.8332 |
| avg_hold_time_bars | 15.8906 |
| exposure | 0.3366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
