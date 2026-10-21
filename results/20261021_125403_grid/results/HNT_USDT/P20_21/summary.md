# EMA Hourly Continuation — HNT/USDT P20_21

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 148 |
| net_profit_factor | 0.4951 |
| net_win_rate | 0.4054 |
| gross_profit_factor | 0.6875 |
| gross_win_rate | 0.4054 |
| sharpe_ratio | -2.6687 |
| sortino_ratio | -0.4611 |
| max_drawdown | 0.4227 |
| cagr | -0.1915 |
| net_avg_win | 67.5844 |
| net_avg_loss | -93.0816 |
| avg_hold_time_bars | 4.3986 |
| exposure | 0.0296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
