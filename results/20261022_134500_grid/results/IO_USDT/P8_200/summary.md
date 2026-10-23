# EMA Hourly Continuation — IO/USDT P8_200

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.5980 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.8172 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -3.2941 |
| sortino_ratio | -0.9306 |
| max_drawdown | 0.6647 |
| cagr | -0.3592 |
| net_avg_win | 56.8715 |
| net_avg_loss | -75.8974 |
| avg_hold_time_bars | 43.3969 |
| exposure | 0.8047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
