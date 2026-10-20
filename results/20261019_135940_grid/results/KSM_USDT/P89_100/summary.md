# EMA Hourly Continuation — KSM/USDT P89_100

**Symbol:** KSM/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.2429 |
| net_win_rate | 0.3765 |
| gross_profit_factor | 0.7475 |
| gross_win_rate | 0.4319 |
| sharpe_ratio | -10.0297 |
| sortino_ratio | -3.5906 |
| max_drawdown | 0.9921 |
| cagr | -0.8531 |
| net_avg_win | 14.2047 |
| net_avg_loss | -35.3124 |
| avg_hold_time_bars | 2.1109 |
| exposure | 0.0571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
