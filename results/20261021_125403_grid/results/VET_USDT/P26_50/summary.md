# EMA Hourly Continuation — VET/USDT P26_50

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.7167 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0275 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -2.0277 |
| sortino_ratio | -0.5757 |
| max_drawdown | 0.4986 |
| cagr | -0.2308 |
| net_avg_win | 61.6525 |
| net_avg_loss | -88.7162 |
| avg_hold_time_bars | 5.6641 |
| exposure | 0.1004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
