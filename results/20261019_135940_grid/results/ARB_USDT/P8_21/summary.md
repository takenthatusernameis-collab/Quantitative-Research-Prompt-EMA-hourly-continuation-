# EMA Hourly Continuation — ARB/USDT P8_21

**Symbol:** ARB/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1678 |
| net_profit_factor | 0.2904 |
| net_win_rate | 0.4362 |
| gross_profit_factor | 0.7427 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -11.4068 |
| sortino_ratio | -6.5930 |
| max_drawdown | 0.9998 |
| cagr | -0.9636 |
| net_avg_win | 5.5882 |
| net_avg_loss | -14.8923 |
| avg_hold_time_bars | 2.8319 |
| exposure | 0.2160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
