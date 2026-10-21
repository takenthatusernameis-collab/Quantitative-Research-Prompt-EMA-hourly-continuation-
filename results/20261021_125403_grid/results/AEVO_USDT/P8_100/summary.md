# EMA Hourly Continuation — AEVO/USDT P8_100

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.8333 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9930 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.2659 |
| sortino_ratio | -0.3840 |
| max_drawdown | 0.4221 |
| cagr | -0.1643 |
| net_avg_win | 80.5554 |
| net_avg_loss | -96.2388 |
| avg_hold_time_bars | 34.5629 |
| exposure | 0.7085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
