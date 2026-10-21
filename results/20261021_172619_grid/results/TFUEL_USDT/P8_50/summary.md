# EMA Hourly Continuation — TFUEL/USDT P8_50

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 836 |
| net_profit_factor | 0.6771 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8946 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -4.5047 |
| sortino_ratio | -1.8477 |
| max_drawdown | 0.8839 |
| cagr | -0.5723 |
| net_avg_win | 49.0907 |
| net_avg_loss | -59.5504 |
| avg_hold_time_bars | 9.7081 |
| exposure | 0.3673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
