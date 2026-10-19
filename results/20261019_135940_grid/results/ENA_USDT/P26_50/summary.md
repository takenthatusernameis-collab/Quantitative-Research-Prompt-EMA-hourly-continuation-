# EMA Hourly Continuation — ENA/USDT P26_50

**Symbol:** ENA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 911 |
| net_profit_factor | 0.5607 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8628 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -5.7719 |
| sortino_ratio | -2.4574 |
| max_drawdown | 0.9507 |
| cagr | -0.6912 |
| net_avg_win | 29.2877 |
| net_avg_loss | -43.3191 |
| avg_hold_time_bars | 3.9989 |
| exposure | 0.1656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
