# EMA Hourly Continuation — ORCA/USDT P89_144

**Symbol:** ORCA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.6736 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -2.0580 |
| sortino_ratio | -0.5080 |
| max_drawdown | 0.4665 |
| cagr | -0.2103 |
| net_avg_win | 62.8029 |
| net_avg_loss | -89.5801 |
| avg_hold_time_bars | 8.9733 |
| exposure | 0.1224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
