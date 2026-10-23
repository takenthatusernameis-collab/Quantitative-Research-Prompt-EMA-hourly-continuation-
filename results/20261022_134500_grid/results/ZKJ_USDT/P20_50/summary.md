# EMA Hourly Continuation — ZKJ/USDT P20_50

**Symbol:** ZKJ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1081 |
| net_profit_factor | 0.1794 |
| net_win_rate | 0.2858 |
| gross_profit_factor | 0.4688 |
| gross_win_rate | 0.3571 |
| sharpe_ratio | -15.4930 |
| sortino_ratio | -7.4638 |
| max_drawdown | 1.0000 |
| cagr | -0.9824 |
| net_avg_win | 7.0726 |
| net_avg_loss | -15.7837 |
| avg_hold_time_bars | 7.9500 |
| exposure | 0.3906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
