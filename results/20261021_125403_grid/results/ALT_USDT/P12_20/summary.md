# EMA Hourly Continuation — ALT/USDT P12_20

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6035 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.8563 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -3.5608 |
| sortino_ratio | -1.1568 |
| max_drawdown | 0.7440 |
| cagr | -0.4125 |
| net_avg_win | 46.7435 |
| net_avg_loss | -67.1064 |
| avg_hold_time_bars | 5.6170 |
| exposure | 0.1320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
