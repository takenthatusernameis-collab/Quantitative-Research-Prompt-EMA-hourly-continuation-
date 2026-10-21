# EMA Hourly Continuation — RLC/USDT P8_100

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.9397 |
| net_win_rate | 0.5372 |
| gross_profit_factor | 1.1534 |
| gross_win_rate | 0.5372 |
| sharpe_ratio | -0.3704 |
| sortino_ratio | -0.1126 |
| max_drawdown | 0.3454 |
| cagr | -0.0564 |
| net_avg_win | 88.8752 |
| net_avg_loss | -109.8007 |
| avg_hold_time_bars | 35.2280 |
| exposure | 0.7094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
