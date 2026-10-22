# EMA Hourly Continuation — AKT/USDT P55_200

**Symbol:** AKT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.7512 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0203 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -1.6424 |
| sortino_ratio | -0.4705 |
| max_drawdown | 0.4351 |
| cagr | -0.1991 |
| net_avg_win | 62.3458 |
| net_avg_loss | -85.9019 |
| avg_hold_time_bars | 18.0713 |
| exposure | 0.3343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
