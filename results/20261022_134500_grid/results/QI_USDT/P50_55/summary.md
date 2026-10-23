# EMA Hourly Continuation — QI/USDT P50_55

**Symbol:** QI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.2339 |
| net_win_rate | 0.3607 |
| gross_profit_factor | 0.7774 |
| gross_win_rate | 0.4416 |
| sharpe_ratio | -11.1491 |
| sortino_ratio | -4.4610 |
| max_drawdown | 0.9975 |
| cagr | -0.9056 |
| net_avg_win | 11.1926 |
| net_avg_loss | -27.0091 |
| avg_hold_time_bars | 2.3740 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
