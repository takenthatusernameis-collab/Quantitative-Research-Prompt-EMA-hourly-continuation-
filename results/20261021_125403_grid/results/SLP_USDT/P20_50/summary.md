# EMA Hourly Continuation — SLP/USDT P20_50

**Symbol:** SLP/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.6829 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.9243 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -3.5872 |
| sortino_ratio | -1.2375 |
| max_drawdown | 0.7729 |
| cagr | -0.4327 |
| net_avg_win | 60.7633 |
| net_avg_loss | -75.7486 |
| avg_hold_time_bars | 6.8889 |
| exposure | 0.1832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
