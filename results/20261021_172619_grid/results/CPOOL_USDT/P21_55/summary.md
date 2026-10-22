# EMA Hourly Continuation — CPOOL/USDT P21_55

**Symbol:** CPOOL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7608 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9218 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.7609 |
| sortino_ratio | -0.5570 |
| max_drawdown | 0.4942 |
| cagr | -0.2271 |
| net_avg_win | 63.3873 |
| net_avg_loss | -79.0204 |
| avg_hold_time_bars | 7.7475 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
