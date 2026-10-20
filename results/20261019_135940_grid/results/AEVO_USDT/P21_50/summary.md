# EMA Hourly Continuation — AEVO/USDT P21_50

**Symbol:** AEVO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 984 |
| net_profit_factor | 0.5234 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8671 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -6.5663 |
| sortino_ratio | -2.9034 |
| max_drawdown | 0.9721 |
| cagr | -0.7517 |
| net_avg_win | 24.1024 |
| net_avg_loss | -37.5562 |
| avg_hold_time_bars | 5.1443 |
| exposure | 0.2291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
