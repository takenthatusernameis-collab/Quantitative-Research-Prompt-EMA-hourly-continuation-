# EMA Hourly Continuation — DYDX/USDT P89_144

**Symbol:** DYDX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.6012 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.9799 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -3.8539 |
| sortino_ratio | -1.2365 |
| max_drawdown | 0.7758 |
| cagr | -0.4392 |
| net_avg_win | 47.9185 |
| net_avg_loss | -72.2141 |
| avg_hold_time_bars | 5.0335 |
| exposure | 0.1160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
