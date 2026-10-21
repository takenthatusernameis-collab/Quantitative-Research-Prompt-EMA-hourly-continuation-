# EMA Hourly Continuation — XYO/USDT P50_89

**Symbol:** XYO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.5459 |
| net_win_rate | 0.4290 |
| gross_profit_factor | 0.7755 |
| gross_win_rate | 0.4290 |
| sharpe_ratio | -3.8387 |
| sortino_ratio | -1.0448 |
| max_drawdown | 0.7114 |
| cagr | -0.3846 |
| net_avg_win | 54.0777 |
| net_avg_loss | -74.4091 |
| avg_hold_time_bars | 8.4727 |
| exposure | 0.1403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
