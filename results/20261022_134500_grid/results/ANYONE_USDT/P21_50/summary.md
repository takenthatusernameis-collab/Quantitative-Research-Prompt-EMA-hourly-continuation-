# EMA Hourly Continuation — ANYONE/USDT P21_50

**Symbol:** ANYONE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 850 |
| net_profit_factor | 0.4595 |
| net_win_rate | 0.3953 |
| gross_profit_factor | 0.6773 |
| gross_win_rate | 0.3988 |
| sharpe_ratio | -7.6510 |
| sortino_ratio | -3.2910 |
| max_drawdown | 0.9730 |
| cagr | -0.7970 |
| net_avg_win | 24.6086 |
| net_avg_loss | -35.0114 |
| avg_hold_time_bars | 4.8635 |
| exposure | 0.2089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
