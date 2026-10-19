# EMA Hourly Continuation — DOT/USDT P50_55

**Symbol:** DOT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 749 |
| net_profit_factor | 0.1639 |
| net_win_rate | 0.3391 |
| gross_profit_factor | 0.6452 |
| gross_win_rate | 0.3885 |
| sharpe_ratio | -12.9253 |
| sortino_ratio | -5.3068 |
| max_drawdown | 0.9994 |
| cagr | -0.9494 |
| net_avg_win | 7.7148 |
| net_avg_loss | -24.1495 |
| avg_hold_time_bars | 1.6822 |
| exposure | 0.0573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
