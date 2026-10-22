# EMA Hourly Continuation — FLR/USDT P12_34

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1469 |
| net_profit_factor | 0.4288 |
| net_win_rate | 0.4118 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -12.2765 |
| sortino_ratio | -6.6380 |
| max_drawdown | 0.9998 |
| cagr | -0.9669 |
| net_avg_win | 12.4074 |
| net_avg_loss | -20.2599 |
| avg_hold_time_bars | 3.7992 |
| exposure | 0.2537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
