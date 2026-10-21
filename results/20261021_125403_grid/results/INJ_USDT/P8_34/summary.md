# EMA Hourly Continuation — INJ/USDT P8_34

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.7559 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9497 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -2.2994 |
| sortino_ratio | -0.8571 |
| max_drawdown | 0.6327 |
| cagr | -0.3257 |
| net_avg_win | 58.5971 |
| net_avg_loss | -73.9588 |
| avg_hold_time_bars | 9.4044 |
| exposure | 0.2907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
