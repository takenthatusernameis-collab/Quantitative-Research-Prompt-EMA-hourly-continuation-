# EMA Hourly Continuation — YGG/USDT P21_26

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1194 |
| net_profit_factor | 0.3446 |
| net_win_rate | 0.3819 |
| gross_profit_factor | 0.8230 |
| gross_win_rate | 0.4238 |
| sharpe_ratio | -12.9432 |
| sortino_ratio | -6.4117 |
| max_drawdown | 0.9998 |
| cagr | -0.9640 |
| net_avg_win | 11.5282 |
| net_avg_loss | -20.6701 |
| avg_hold_time_bars | 1.9916 |
| exposure | 0.1076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
