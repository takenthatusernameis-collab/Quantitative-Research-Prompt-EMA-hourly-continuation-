# EMA Hourly Continuation — SYN/USDT P21_50

**Symbol:** SYN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 960 |
| net_profit_factor | 0.5177 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8307 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -6.3840 |
| sortino_ratio | -2.7726 |
| max_drawdown | 0.9669 |
| cagr | -0.7410 |
| net_avg_win | 24.1200 |
| net_avg_loss | -37.8024 |
| avg_hold_time_bars | 5.2687 |
| exposure | 0.2299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
