# EMA Hourly Continuation — JTO/USDT P26_89

**Symbol:** JTO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7551 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9164 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -2.1226 |
| sortino_ratio | -0.6633 |
| max_drawdown | 0.5833 |
| cagr | -0.2631 |
| net_avg_win | 72.7281 |
| net_avg_loss | -85.7376 |
| avg_hold_time_bars | 13.1369 |
| exposure | 0.2878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
