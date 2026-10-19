# EMA Hourly Continuation — SUI/USDT P21_100

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.5895 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.9002 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -4.8720 |
| sortino_ratio | -1.7575 |
| max_drawdown | 0.8985 |
| cagr | -0.5824 |
| net_avg_win | 41.8254 |
| net_avg_loss | -59.1280 |
| avg_hold_time_bars | 12.9165 |
| exposure | 0.3940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
