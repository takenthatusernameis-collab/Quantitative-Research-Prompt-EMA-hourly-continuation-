# EMA Hourly Continuation — JTO/USDT P8_12

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1877 |
| net_profit_factor | 0.2774 |
| net_win_rate | 0.3969 |
| gross_profit_factor | 0.6958 |
| gross_win_rate | 0.4315 |
| sharpe_ratio | -15.4241 |
| sortino_ratio | -9.5005 |
| max_drawdown | 1.0000 |
| cagr | -0.9928 |
| net_avg_win | 5.1521 |
| net_avg_loss | -12.2246 |
| avg_hold_time_bars | 1.8918 |
| exposure | 0.1614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
