# EMA Hourly Continuation — XAI/USDT P50_55

**Symbol:** XAI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 171 |
| net_profit_factor | 0.6063 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.8584 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -2.0630 |
| sortino_ratio | -0.3855 |
| max_drawdown | 0.3977 |
| cagr | -0.1616 |
| net_avg_win | 69.6904 |
| net_avg_loss | -98.7091 |
| avg_hold_time_bars | 4.4854 |
| exposure | 0.0349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
