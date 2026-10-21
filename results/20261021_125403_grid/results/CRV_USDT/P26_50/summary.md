# EMA Hourly Continuation — CRV/USDT P26_50

**Symbol:** CRV/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.8120 |
| net_win_rate | 0.5202 |
| gross_profit_factor | 1.0772 |
| gross_win_rate | 0.5202 |
| sharpe_ratio | -1.2779 |
| sortino_ratio | -0.3665 |
| max_drawdown | 0.3886 |
| cagr | -0.1552 |
| net_avg_win | 72.4094 |
| net_avg_loss | -96.6805 |
| avg_hold_time_bars | 5.4343 |
| exposure | 0.0978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
