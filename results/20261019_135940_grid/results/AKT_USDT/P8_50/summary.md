# EMA Hourly Continuation — AKT/USDT P8_50

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1090 |
| net_profit_factor | 0.5388 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8983 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -6.1862 |
| sortino_ratio | -2.8604 |
| max_drawdown | 0.9708 |
| cagr | -0.7506 |
| net_avg_win | 22.6486 |
| net_avg_loss | -35.6248 |
| avg_hold_time_bars | 8.8945 |
| exposure | 0.4407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
