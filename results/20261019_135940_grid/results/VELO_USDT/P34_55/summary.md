# EMA Hourly Continuation — VELO/USDT P34_55

**Symbol:** VELO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 900 |
| net_profit_factor | 0.5008 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.8347 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -7.2098 |
| sortino_ratio | -3.0522 |
| max_drawdown | 0.9774 |
| cagr | -0.7747 |
| net_avg_win | 24.7940 |
| net_avg_loss | -38.7262 |
| avg_hold_time_bars | 3.2933 |
| exposure | 0.1347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
