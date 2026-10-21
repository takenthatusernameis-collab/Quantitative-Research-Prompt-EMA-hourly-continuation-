# EMA Hourly Continuation — ORCA/USDT P50_89

**Symbol:** ORCA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6631 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9289 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -2.3850 |
| sortino_ratio | -0.6616 |
| max_drawdown | 0.5652 |
| cagr | -0.2614 |
| net_avg_win | 57.2971 |
| net_avg_loss | -81.9364 |
| avg_hold_time_bars | 8.4255 |
| exposure | 0.1440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
