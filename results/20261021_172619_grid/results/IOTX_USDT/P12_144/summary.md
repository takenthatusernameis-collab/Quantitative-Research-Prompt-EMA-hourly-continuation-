# EMA Hourly Continuation — IOTX/USDT P12_144

**Symbol:** IOTX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7551 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9196 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -1.6123 |
| sortino_ratio | -0.4443 |
| max_drawdown | 0.4078 |
| cagr | -0.1855 |
| net_avg_win | 68.5961 |
| net_avg_loss | -85.1973 |
| avg_hold_time_bars | 39.1524 |
| exposure | 0.6656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
