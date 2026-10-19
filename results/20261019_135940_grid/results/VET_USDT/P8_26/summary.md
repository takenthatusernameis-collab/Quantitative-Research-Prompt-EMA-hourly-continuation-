# EMA Hourly Continuation — VET/USDT P8_26

**Symbol:** VET/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1561 |
| net_profit_factor | 0.3938 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.8285 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -11.1972 |
| sortino_ratio | -6.2276 |
| max_drawdown | 0.9996 |
| cagr | -0.9566 |
| net_avg_win | 9.6488 |
| net_avg_loss | -18.5697 |
| avg_hold_time_bars | 3.7034 |
| exposure | 0.2628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
