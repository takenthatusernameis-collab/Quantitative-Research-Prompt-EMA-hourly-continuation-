# EMA Hourly Continuation — BOME/USDT P8_12

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1809 |
| net_profit_factor | 0.3097 |
| net_win_rate | 0.3803 |
| gross_profit_factor | 0.7295 |
| gross_win_rate | 0.4063 |
| sharpe_ratio | -16.0904 |
| sortino_ratio | -9.7841 |
| max_drawdown | 1.0000 |
| cagr | -0.9941 |
| net_avg_win | 6.5216 |
| net_avg_loss | -12.9231 |
| avg_hold_time_bars | 1.7728 |
| exposure | 0.1458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
