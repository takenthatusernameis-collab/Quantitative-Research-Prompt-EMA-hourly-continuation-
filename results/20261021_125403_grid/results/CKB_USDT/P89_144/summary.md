# EMA Hourly Continuation — CKB/USDT P89_144

**Symbol:** CKB/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.7246 |
| net_win_rate | 0.5062 |
| gross_profit_factor | 0.9941 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -1.6973 |
| sortino_ratio | -0.4360 |
| max_drawdown | 0.4108 |
| cagr | -0.1815 |
| net_avg_win | 64.1888 |
| net_avg_loss | -90.8307 |
| avg_hold_time_bars | 7.6562 |
| exposure | 0.1114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
