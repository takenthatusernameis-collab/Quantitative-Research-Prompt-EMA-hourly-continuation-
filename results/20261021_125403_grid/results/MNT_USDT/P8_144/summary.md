# EMA Hourly Continuation — MNT/USDT P8_144

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 1.0157 |
| net_win_rate | 0.5524 |
| gross_profit_factor | 1.2249 |
| gross_win_rate | 0.5524 |
| sharpe_ratio | 0.1415 |
| sortino_ratio | 0.0365 |
| max_drawdown | 0.1799 |
| cagr | 0.0096 |
| net_avg_win | 90.5145 |
| net_avg_loss | -109.9717 |
| avg_hold_time_bars | 54.5778 |
| exposure | 0.7815 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
