# EMA Hourly Continuation — AIOZ/USDT P50_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.9002 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0592 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -0.6525 |
| sortino_ratio | -0.1647 |
| max_drawdown | 0.3366 |
| cagr | -0.0759 |
| net_avg_win | 102.0677 |
| net_avg_loss | -119.3861 |
| avg_hold_time_bars | 27.1645 |
| exposure | 0.3828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
