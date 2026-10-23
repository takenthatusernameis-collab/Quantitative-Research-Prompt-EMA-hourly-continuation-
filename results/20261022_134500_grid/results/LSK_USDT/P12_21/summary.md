# EMA Hourly Continuation — LSK/USDT P12_21

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1148 |
| net_profit_factor | 0.3781 |
| net_win_rate | 0.4199 |
| gross_profit_factor | 0.9298 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -10.4257 |
| sortino_ratio | -5.0461 |
| max_drawdown | 0.9982 |
| cagr | -0.9197 |
| net_avg_win | 12.5896 |
| net_avg_loss | -24.0997 |
| avg_hold_time_bars | 3.4660 |
| exposure | 0.1809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
