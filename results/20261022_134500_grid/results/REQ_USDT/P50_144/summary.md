# EMA Hourly Continuation — REQ/USDT P50_144

**Symbol:** REQ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.4312 |
| net_win_rate | 0.4003 |
| gross_profit_factor | 0.8510 |
| gross_win_rate | 0.4214 |
| sharpe_ratio | -7.6620 |
| sortino_ratio | -2.7119 |
| max_drawdown | 0.9663 |
| cagr | -0.7380 |
| net_avg_win | 29.6309 |
| net_avg_loss | -45.8719 |
| avg_hold_time_bars | 9.6937 |
| exposure | 0.2719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
