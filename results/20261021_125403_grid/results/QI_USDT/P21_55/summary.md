# EMA Hourly Continuation — QI/USDT P21_55

**Symbol:** QI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.7318 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0214 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -2.4389 |
| sortino_ratio | -0.8432 |
| max_drawdown | 0.6532 |
| cagr | -0.3194 |
| net_avg_win | 57.8341 |
| net_avg_loss | -80.1274 |
| avg_hold_time_bars | 8.0498 |
| exposure | 0.2120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
