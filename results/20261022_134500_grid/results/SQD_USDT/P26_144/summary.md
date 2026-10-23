# EMA Hourly Continuation — SQD/USDT P26_144

**Symbol:** SQD/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.7909 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0506 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -1.6792 |
| sortino_ratio | -0.5389 |
| max_drawdown | 0.5041 |
| cagr | -0.2264 |
| net_avg_win | 69.3762 |
| net_avg_loss | -90.9501 |
| avg_hold_time_bars | 19.1107 |
| exposure | 0.4464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
