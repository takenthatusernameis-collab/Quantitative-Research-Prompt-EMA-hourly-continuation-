# EMA Hourly Continuation — BAND/USDT P20_55

**Symbol:** BAND/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.7182 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9750 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -3.1664 |
| sortino_ratio | -1.1455 |
| max_drawdown | 0.7582 |
| cagr | -0.4091 |
| net_avg_win | 60.4105 |
| net_avg_loss | -78.0694 |
| avg_hold_time_bars | 8.6165 |
| exposure | 0.2511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
