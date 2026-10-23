# EMA Hourly Continuation — QI/USDT P8_100

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6803 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9696 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -3.2019 |
| sortino_ratio | -1.1152 |
| max_drawdown | 0.7639 |
| cagr | -0.4081 |
| net_avg_win | 53.0917 |
| net_avg_loss | -72.8436 |
| avg_hold_time_bars | 23.6535 |
| exposure | 0.6518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
