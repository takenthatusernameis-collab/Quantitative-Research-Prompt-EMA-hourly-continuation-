# EMA Hourly Continuation — SOL/USDT P89_200

**Symbol:** SOL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.6613 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.8856 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -2.1571 |
| sortino_ratio | -0.5001 |
| max_drawdown | 0.4533 |
| cagr | -0.2052 |
| net_avg_win | 69.0092 |
| net_avg_loss | -92.4280 |
| avg_hold_time_bars | 14.2765 |
| exposure | 0.1713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
