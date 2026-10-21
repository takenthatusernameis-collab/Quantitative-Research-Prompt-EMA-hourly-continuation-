# EMA Hourly Continuation — ATOM/USDT P20_26

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 136 |
| net_profit_factor | 0.4996 |
| net_win_rate | 0.4118 |
| gross_profit_factor | 0.7213 |
| gross_win_rate | 0.4118 |
| sharpe_ratio | -2.6026 |
| sortino_ratio | -0.4336 |
| max_drawdown | 0.4093 |
| cagr | -0.1824 |
| net_avg_win | 70.7564 |
| net_avg_loss | -99.1469 |
| avg_hold_time_bars | 5.3309 |
| exposure | 0.0330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
