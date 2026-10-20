# EMA Hourly Continuation — FIDA/USDT P100_200

**Symbol:** FIDA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.5766 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.8508 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -3.5075 |
| sortino_ratio | -1.0345 |
| max_drawdown | 0.7126 |
| cagr | -0.3845 |
| net_avg_win | 48.8143 |
| net_avg_loss | -70.0687 |
| avg_hold_time_bars | 9.7379 |
| exposure | 0.1917 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
