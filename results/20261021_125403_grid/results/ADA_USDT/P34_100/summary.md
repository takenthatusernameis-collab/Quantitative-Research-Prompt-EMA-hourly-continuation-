# EMA Hourly Continuation — ADA/USDT P34_100

**Symbol:** ADA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.7370 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9598 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -1.9165 |
| sortino_ratio | -0.5604 |
| max_drawdown | 0.4928 |
| cagr | -0.2271 |
| net_avg_win | 64.8116 |
| net_avg_loss | -85.4451 |
| avg_hold_time_bars | 12.4187 |
| exposure | 0.2360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
