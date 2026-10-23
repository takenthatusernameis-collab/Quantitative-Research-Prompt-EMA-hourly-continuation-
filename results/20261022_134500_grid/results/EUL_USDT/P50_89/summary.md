# EMA Hourly Continuation — EUL/USDT P50_89

**Symbol:** EUL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.3189 |
| net_win_rate | 0.3895 |
| gross_profit_factor | 0.5711 |
| gross_win_rate | 0.4048 |
| sharpe_ratio | -6.9354 |
| sortino_ratio | -2.3673 |
| max_drawdown | 0.9487 |
| cagr | -0.6901 |
| net_avg_win | 19.3699 |
| net_avg_loss | -38.7419 |
| avg_hold_time_bars | 5.7245 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
