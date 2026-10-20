# EMA Hourly Continuation — DYDX/USDT P12_26

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1392 |
| net_profit_factor | 0.4200 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.9115 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -10.3649 |
| sortino_ratio | -5.4502 |
| max_drawdown | 0.9989 |
| cagr | -0.9339 |
| net_avg_win | 11.9743 |
| net_avg_loss | -21.8548 |
| avg_hold_time_bars | 2.9066 |
| exposure | 0.1839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
