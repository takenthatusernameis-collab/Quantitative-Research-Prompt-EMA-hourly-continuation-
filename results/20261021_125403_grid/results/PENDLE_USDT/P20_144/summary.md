# EMA Hourly Continuation — PENDLE/USDT P20_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.8188 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9504 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.1086 |
| sortino_ratio | -0.2958 |
| max_drawdown | 0.3551 |
| cagr | -0.1288 |
| net_avg_win | 77.3707 |
| net_avg_loss | -90.7717 |
| avg_hold_time_bars | 36.0888 |
| exposure | 0.5725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
