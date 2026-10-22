# EMA Hourly Continuation — REZ/USDT P8_50

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.8809 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0675 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -1.1870 |
| sortino_ratio | -0.4592 |
| max_drawdown | 0.5163 |
| cagr | -0.1948 |
| net_avg_win | 83.3881 |
| net_avg_loss | -100.6836 |
| avg_hold_time_bars | 13.1849 |
| exposure | 0.4343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
