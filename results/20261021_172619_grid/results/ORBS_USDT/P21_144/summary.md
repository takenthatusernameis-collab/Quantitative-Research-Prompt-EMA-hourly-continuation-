# EMA Hourly Continuation — ORBS/USDT P21_144

**Symbol:** ORBS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.7371 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9603 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.2380 |
| sortino_ratio | -0.6468 |
| max_drawdown | 0.5869 |
| cagr | -0.2576 |
| net_avg_win | 74.5812 |
| net_avg_loss | -93.6155 |
| avg_hold_time_bars | 29.5000 |
| exposure | 0.5525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
