# EMA Hourly Continuation — AR/USDT P21_55

**Symbol:** AR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.7400 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 0.9349 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -1.9529 |
| sortino_ratio | -0.6252 |
| max_drawdown | 0.5344 |
| cagr | -0.2498 |
| net_avg_win | 59.4808 |
| net_avg_loss | -77.5453 |
| avg_hold_time_bars | 8.2535 |
| exposure | 0.1880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
