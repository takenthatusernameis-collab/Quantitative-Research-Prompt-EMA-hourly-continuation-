# EMA Hourly Continuation — BAT/USDT P12_20

**Symbol:** BAT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.5773 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9411 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -3.9221 |
| sortino_ratio | -1.2186 |
| max_drawdown | 0.7552 |
| cagr | -0.4290 |
| net_avg_win | 46.6752 |
| net_avg_loss | -72.3374 |
| avg_hold_time_bars | 4.6474 |
| exposure | 0.0989 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
