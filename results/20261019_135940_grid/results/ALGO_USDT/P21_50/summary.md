# EMA Hourly Continuation — ALGO/USDT P21_50

**Symbol:** ALGO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 981 |
| net_profit_factor | 0.4948 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9458 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -6.2736 |
| sortino_ratio | -2.7638 |
| max_drawdown | 0.9676 |
| cagr | -0.7397 |
| net_avg_win | 19.9602 |
| net_avg_loss | -37.7132 |
| avg_hold_time_bars | 4.2039 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
