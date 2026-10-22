# EMA Hourly Continuation — SYN/USDT P55_144

**Symbol:** SYN/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.6850 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.8407 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -2.0358 |
| sortino_ratio | -0.5245 |
| max_drawdown | 0.4604 |
| cagr | -0.2151 |
| net_avg_win | 65.1757 |
| net_avg_loss | -81.7118 |
| avg_hold_time_bars | 18.7508 |
| exposure | 0.2804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
