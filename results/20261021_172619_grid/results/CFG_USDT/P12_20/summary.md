# EMA Hourly Continuation — CFG/USDT P12_20

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.6354 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.8561 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -2.3598 |
| sortino_ratio | -0.5937 |
| max_drawdown | 0.5032 |
| cagr | -0.2382 |
| net_avg_win | 59.5143 |
| net_avg_loss | -81.8093 |
| avg_hold_time_bars | 4.8489 |
| exposure | 0.0685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
