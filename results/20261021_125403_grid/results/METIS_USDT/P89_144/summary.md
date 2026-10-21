# EMA Hourly Continuation — METIS/USDT P89_144

**Symbol:** METIS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.6669 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8730 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -2.3689 |
| sortino_ratio | -0.5844 |
| max_drawdown | 0.5119 |
| cagr | -0.2357 |
| net_avg_win | 71.2122 |
| net_avg_loss | -90.9597 |
| avg_hold_time_bars | 8.1233 |
| exposure | 0.1108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
