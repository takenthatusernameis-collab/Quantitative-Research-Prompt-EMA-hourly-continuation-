# EMA Hourly Continuation — AEVO/USDT P12_100

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.8268 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 1.0002 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.3930 |
| sortino_ratio | -0.4237 |
| max_drawdown | 0.4572 |
| cagr | -0.1792 |
| net_avg_win | 82.8789 |
| net_avg_loss | -98.9257 |
| avg_hold_time_bars | 29.5055 |
| exposure | 0.6075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
