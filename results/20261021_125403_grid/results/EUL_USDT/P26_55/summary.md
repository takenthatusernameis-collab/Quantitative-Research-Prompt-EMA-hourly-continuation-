# EMA Hourly Continuation — EUL/USDT P26_55

**Symbol:** EUL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.5952 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.7925 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -2.8810 |
| sortino_ratio | -0.8571 |
| max_drawdown | 0.6413 |
| cagr | -0.3256 |
| net_avg_win | 45.9579 |
| net_avg_loss | -66.0405 |
| avg_hold_time_bars | 7.6468 |
| exposure | 0.1515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
