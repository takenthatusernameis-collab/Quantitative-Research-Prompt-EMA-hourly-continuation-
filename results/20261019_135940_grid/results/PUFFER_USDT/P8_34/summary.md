# EMA Hourly Continuation — PUFFER/USDT P8_34

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 984 |
| net_profit_factor | 0.5720 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8762 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -5.8884 |
| sortino_ratio | -2.8924 |
| max_drawdown | 0.9415 |
| cagr | -0.7519 |
| net_avg_win | 27.2442 |
| net_avg_loss | -41.9854 |
| avg_hold_time_bars | 6.5051 |
| exposure | 0.3622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
