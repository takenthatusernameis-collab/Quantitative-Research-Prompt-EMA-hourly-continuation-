# EMA Hourly Continuation — ORBS/USDT P8_50

**Symbol:** ORBS/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 758 |
| net_profit_factor | 0.5922 |
| net_win_rate | 0.4195 |
| gross_profit_factor | 0.8157 |
| gross_win_rate | 0.4195 |
| sharpe_ratio | -5.6985 |
| sortino_ratio | -2.2250 |
| max_drawdown | 0.9273 |
| cagr | -0.6438 |
| net_avg_win | 42.2514 |
| net_avg_loss | -51.5626 |
| avg_hold_time_bars | 12.9433 |
| exposure | 0.4460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
