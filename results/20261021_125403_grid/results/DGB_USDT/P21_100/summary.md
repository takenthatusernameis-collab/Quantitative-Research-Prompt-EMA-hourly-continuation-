# EMA Hourly Continuation — DGB/USDT P21_100

**Symbol:** DGB/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7388 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9239 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -2.0410 |
| sortino_ratio | -0.6452 |
| max_drawdown | 0.5302 |
| cagr | -0.2570 |
| net_avg_win | 62.7281 |
| net_avg_loss | -79.2264 |
| avg_hold_time_bars | 16.5234 |
| exposure | 0.3688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
