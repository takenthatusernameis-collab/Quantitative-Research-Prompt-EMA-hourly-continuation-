# EMA Hourly Continuation — REQ/USDT P34_100

**Symbol:** REQ/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.6826 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 1.0116 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -2.9210 |
| sortino_ratio | -0.8985 |
| max_drawdown | 0.6518 |
| cagr | -0.3385 |
| net_avg_win | 61.4538 |
| net_avg_loss | -86.5807 |
| avg_hold_time_bars | 12.1540 |
| exposure | 0.2547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
