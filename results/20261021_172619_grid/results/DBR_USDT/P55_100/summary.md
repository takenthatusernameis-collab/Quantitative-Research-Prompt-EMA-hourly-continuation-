# EMA Hourly Continuation — DBR/USDT P55_100

**Symbol:** DBR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.5803 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8496 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -3.1903 |
| sortino_ratio | -0.8110 |
| max_drawdown | 0.5477 |
| cagr | -0.3114 |
| net_avg_win | 63.3678 |
| net_avg_loss | -90.3504 |
| avg_hold_time_bars | 9.6220 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
