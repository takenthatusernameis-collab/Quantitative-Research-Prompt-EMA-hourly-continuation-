# EMA Hourly Continuation — ZETA/USDT P21_100

**Symbol:** ZETA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.8498 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0493 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -1.2817 |
| sortino_ratio | -0.3979 |
| max_drawdown | 0.5170 |
| cagr | -0.1694 |
| net_avg_win | 88.4958 |
| net_avg_loss | -107.2836 |
| avg_hold_time_bars | 19.6921 |
| exposure | 0.4197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
