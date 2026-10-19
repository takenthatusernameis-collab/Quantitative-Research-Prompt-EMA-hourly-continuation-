# EMA Hourly Continuation — ONDO/USDT P8_20

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1688 |
| net_profit_factor | 0.3802 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.7481 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -11.2697 |
| sortino_ratio | -6.5200 |
| max_drawdown | 0.9997 |
| cagr | -0.9627 |
| net_avg_win | 8.2882 |
| net_avg_loss | -17.0155 |
| avg_hold_time_bars | 2.6736 |
| exposure | 0.2051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
