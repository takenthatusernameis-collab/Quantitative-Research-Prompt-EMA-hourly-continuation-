# EMA Hourly Continuation — LTC/USDT P34_100

**Symbol:** LTC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.5943 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8272 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -2.9433 |
| sortino_ratio | -0.8284 |
| max_drawdown | 0.6386 |
| cagr | -0.3164 |
| net_avg_win | 50.0650 |
| net_avg_loss | -72.5551 |
| avg_hold_time_bars | 14.4190 |
| exposure | 0.2550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
