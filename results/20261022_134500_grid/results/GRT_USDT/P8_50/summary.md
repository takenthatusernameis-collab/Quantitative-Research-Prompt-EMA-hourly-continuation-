# EMA Hourly Continuation — GRT/USDT P8_50

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1104 |
| net_profit_factor | 0.6095 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.9732 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -6.4271 |
| sortino_ratio | -2.9848 |
| max_drawdown | 0.9752 |
| cagr | -0.7668 |
| net_avg_win | 29.8859 |
| net_avg_loss | -41.9459 |
| avg_hold_time_bars | 9.0054 |
| exposure | 0.4499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
