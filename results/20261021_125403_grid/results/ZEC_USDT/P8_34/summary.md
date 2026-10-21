# EMA Hourly Continuation — ZEC/USDT P8_34

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.7369 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9216 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -2.1322 |
| sortino_ratio | -0.7891 |
| max_drawdown | 0.6033 |
| cagr | -0.3054 |
| net_avg_win | 51.1845 |
| net_avg_loss | -66.4243 |
| avg_hold_time_bars | 8.8405 |
| exposure | 0.2696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
