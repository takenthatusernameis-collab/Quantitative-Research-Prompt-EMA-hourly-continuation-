# EMA Hourly Continuation — AVAX/USDT P50_100

**Symbol:** AVAX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.5382 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -6.0839 |
| sortino_ratio | -2.1127 |
| max_drawdown | 0.9339 |
| cagr | -0.6553 |
| net_avg_win | 39.4548 |
| net_avg_loss | -60.0028 |
| avg_hold_time_bars | 5.3846 |
| exposure | 0.1495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
