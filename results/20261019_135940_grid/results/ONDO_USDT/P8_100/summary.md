# EMA Hourly Continuation — ONDO/USDT P8_100

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.6453 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.9301 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -4.2556 |
| sortino_ratio | -1.6264 |
| max_drawdown | 0.8650 |
| cagr | -0.5437 |
| net_avg_win | 45.2562 |
| net_avg_loss | -61.1193 |
| avg_hold_time_bars | 18.0794 |
| exposure | 0.6106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
