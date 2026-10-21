# EMA Hourly Continuation — HTX/USDT P21_50

**Symbol:** HTX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.3705 |
| net_win_rate | 0.3776 |
| gross_profit_factor | 0.6568 |
| gross_win_rate | 0.3873 |
| sharpe_ratio | -7.4393 |
| sortino_ratio | -2.4570 |
| max_drawdown | 0.9461 |
| cagr | -0.6859 |
| net_avg_win | 28.4115 |
| net_avg_loss | -46.5324 |
| avg_hold_time_bars | 9.1888 |
| exposure | 0.2158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
