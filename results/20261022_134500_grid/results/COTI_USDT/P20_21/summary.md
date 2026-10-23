# EMA Hourly Continuation — COTI/USDT P20_21

**Symbol:** COTI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1248 |
| net_profit_factor | 0.1975 |
| net_win_rate | 0.3117 |
| gross_profit_factor | 0.7163 |
| gross_win_rate | 0.3694 |
| sharpe_ratio | -17.2231 |
| sortino_ratio | -9.0401 |
| max_drawdown | 1.0000 |
| cagr | -0.9942 |
| net_avg_win | 6.3264 |
| net_avg_loss | -14.5063 |
| avg_hold_time_bars | 1.5537 |
| exposure | 0.0881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
