# EMA Hourly Continuation — MERL/USDT P26_55

**Symbol:** MERL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 898 |
| net_profit_factor | 0.4552 |
| net_win_rate | 0.4287 |
| gross_profit_factor | 0.6817 |
| gross_win_rate | 0.4321 |
| sharpe_ratio | -6.5540 |
| sortino_ratio | -2.7730 |
| max_drawdown | 0.9658 |
| cagr | -0.7362 |
| net_avg_win | 20.9315 |
| net_avg_loss | -34.5095 |
| avg_hold_time_bars | 4.9232 |
| exposure | 0.2015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
