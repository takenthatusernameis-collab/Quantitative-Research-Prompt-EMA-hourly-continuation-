# EMA Hourly Continuation — SHIB/USDT P12_100

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 759 |
| net_profit_factor | 0.5944 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.9407 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -5.2863 |
| sortino_ratio | -2.0306 |
| max_drawdown | 0.9251 |
| cagr | -0.6344 |
| net_avg_win | 38.2038 |
| net_avg_loss | -55.8789 |
| avg_hold_time_bars | 15.0856 |
| exposure | 0.5205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
