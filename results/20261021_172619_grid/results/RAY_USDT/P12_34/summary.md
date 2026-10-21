# EMA Hourly Continuation — RAY/USDT P12_34

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.8060 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0461 |
| gross_win_rate | 0.5088 |
| sharpe_ratio | -1.8664 |
| sortino_ratio | -0.6694 |
| max_drawdown | 0.5800 |
| cagr | -0.2660 |
| net_avg_win | 70.9729 |
| net_avg_loss | -90.0553 |
| avg_hold_time_bars | 6.5904 |
| exposure | 0.1872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
