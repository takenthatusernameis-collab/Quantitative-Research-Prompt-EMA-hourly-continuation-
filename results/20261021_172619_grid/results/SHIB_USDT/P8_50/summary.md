# EMA Hourly Continuation — SHIB/USDT P8_50

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7423 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -2.4276 |
| sortino_ratio | -0.9004 |
| max_drawdown | 0.6551 |
| cagr | -0.3386 |
| net_avg_win | 55.8725 |
| net_avg_loss | -74.3768 |
| avg_hold_time_bars | 13.4433 |
| exposure | 0.4094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
