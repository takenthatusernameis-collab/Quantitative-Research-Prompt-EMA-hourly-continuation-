# EMA Hourly Continuation — XTZ/USDT P34_50

**Symbol:** XTZ/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.5354 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.8340 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -3.4585 |
| sortino_ratio | -0.8826 |
| max_drawdown | 0.6400 |
| cagr | -0.3321 |
| net_avg_win | 51.3468 |
| net_avg_loss | -79.2674 |
| avg_hold_time_bars | 5.1203 |
| exposure | 0.0735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
