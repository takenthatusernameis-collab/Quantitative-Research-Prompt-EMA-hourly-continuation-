# EMA Hourly Continuation — BLUR/USDT P21_89

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.6546 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.9873 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -3.9227 |
| sortino_ratio | -1.4394 |
| max_drawdown | 0.8396 |
| cagr | -0.4968 |
| net_avg_win | 47.8451 |
| net_avg_loss | -67.5047 |
| avg_hold_time_bars | 12.9764 |
| exposure | 0.3987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
