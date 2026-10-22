# EMA Hourly Continuation — 1INCH/USDT P34_50

**Symbol:** 1INCH/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 986 |
| net_profit_factor | 0.3580 |
| net_win_rate | 0.4138 |
| gross_profit_factor | 0.8168 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -9.9856 |
| sortino_ratio | -4.4842 |
| max_drawdown | 0.9966 |
| cagr | -0.8947 |
| net_avg_win | 13.6210 |
| net_avg_loss | -26.8552 |
| avg_hold_time_bars | 2.6329 |
| exposure | 0.1180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
