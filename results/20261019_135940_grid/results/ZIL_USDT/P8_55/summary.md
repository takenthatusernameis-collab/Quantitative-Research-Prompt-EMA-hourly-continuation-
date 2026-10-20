# EMA Hourly Continuation — ZIL/USDT P8_55

**Symbol:** ZIL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.5500 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -5.4363 |
| sortino_ratio | -2.4005 |
| max_drawdown | 0.9519 |
| cagr | -0.6858 |
| net_avg_win | 24.3213 |
| net_avg_loss | -41.3513 |
| avg_hold_time_bars | 11.4446 |
| exposure | 0.5114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
