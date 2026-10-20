# EMA Hourly Continuation — ID/USDT P8_26

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1329 |
| net_profit_factor | 0.4936 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 1.0013 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -8.8211 |
| sortino_ratio | -4.5033 |
| max_drawdown | 0.9966 |
| cagr | -0.8915 |
| net_avg_win | 16.7120 |
| net_avg_loss | -26.3005 |
| avg_hold_time_bars | 4.9503 |
| exposure | 0.2977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
