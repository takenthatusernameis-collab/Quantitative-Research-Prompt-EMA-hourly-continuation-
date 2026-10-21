# EMA Hourly Continuation — DBR/USDT P8_34

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.6839 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9897 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -3.6822 |
| sortino_ratio | -1.3956 |
| max_drawdown | 0.7561 |
| cagr | -0.4728 |
| net_avg_win | 57.3286 |
| net_avg_loss | -78.6415 |
| avg_hold_time_bars | 10.0674 |
| exposure | 0.3229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
