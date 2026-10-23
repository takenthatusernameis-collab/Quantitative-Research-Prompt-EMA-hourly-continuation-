# EMA Hourly Continuation — LSK/USDT P21_50

**Symbol:** LSK/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.5045 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -5.8735 |
| sortino_ratio | -2.3632 |
| max_drawdown | 0.9441 |
| cagr | -0.6770 |
| net_avg_win | 25.2902 |
| net_avg_loss | -44.1848 |
| avg_hold_time_bars | 6.2608 |
| exposure | 0.2302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
