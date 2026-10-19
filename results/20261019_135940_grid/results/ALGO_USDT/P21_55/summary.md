# EMA Hourly Continuation — ALGO/USDT P21_55

**Symbol:** ALGO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.5247 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9445 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -6.0023 |
| sortino_ratio | -2.5916 |
| max_drawdown | 0.9590 |
| cagr | -0.7134 |
| net_avg_win | 23.7299 |
| net_avg_loss | -41.1583 |
| avg_hold_time_bars | 4.9925 |
| exposure | 0.2120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
