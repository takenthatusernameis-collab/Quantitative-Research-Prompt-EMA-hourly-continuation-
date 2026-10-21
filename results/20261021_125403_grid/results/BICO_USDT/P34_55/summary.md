# EMA Hourly Continuation — BICO/USDT P34_55

**Symbol:** BICO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.5688 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.7988 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -3.3968 |
| sortino_ratio | -1.0373 |
| max_drawdown | 0.7040 |
| cagr | -0.3772 |
| net_avg_win | 43.9067 |
| net_avg_loss | -64.7882 |
| avg_hold_time_bars | 6.2162 |
| exposure | 0.1294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
