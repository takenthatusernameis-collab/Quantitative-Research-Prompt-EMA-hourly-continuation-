# EMA Hourly Continuation — GMX/USDT P55_100

**Symbol:** GMX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.5787 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8073 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -3.4068 |
| sortino_ratio | -0.9828 |
| max_drawdown | 0.6863 |
| cagr | -0.3635 |
| net_avg_win | 50.6336 |
| net_avg_loss | -71.2412 |
| avg_hold_time_bars | 8.2805 |
| exposure | 0.1543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
