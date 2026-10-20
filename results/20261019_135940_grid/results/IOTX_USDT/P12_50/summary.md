# EMA Hourly Continuation — IOTX/USDT P12_50

**Symbol:** IOTX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1028 |
| net_profit_factor | 0.5809 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.9523 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -6.2874 |
| sortino_ratio | -2.8472 |
| max_drawdown | 0.9686 |
| cagr | -0.7454 |
| net_avg_win | 28.2990 |
| net_avg_loss | -41.6818 |
| avg_hold_time_bars | 7.6226 |
| exposure | 0.3562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
