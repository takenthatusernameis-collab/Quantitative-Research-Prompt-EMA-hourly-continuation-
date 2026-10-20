# EMA Hourly Continuation — ID/USDT P34_100

**Symbol:** ID/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.5529 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8691 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -4.3313 |
| sortino_ratio | -1.5362 |
| max_drawdown | 0.8395 |
| cagr | -0.5142 |
| net_avg_win | 35.9807 |
| net_avg_loss | -54.3296 |
| avg_hold_time_bars | 9.2859 |
| exposure | 0.2660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
