# EMA Hourly Continuation — SUI/USDT P20_100

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.6002 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.9120 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -4.8444 |
| sortino_ratio | -1.7673 |
| max_drawdown | 0.8975 |
| cagr | -0.5850 |
| net_avg_win | 42.5643 |
| net_avg_loss | -59.6964 |
| avg_hold_time_bars | 12.7787 |
| exposure | 0.3990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
