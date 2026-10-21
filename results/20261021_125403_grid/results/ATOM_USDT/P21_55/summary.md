# EMA Hourly Continuation — ATOM/USDT P21_55

**Symbol:** ATOM/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.6583 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9071 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -2.8152 |
| sortino_ratio | -0.8911 |
| max_drawdown | 0.6534 |
| cagr | -0.3349 |
| net_avg_win | 52.7576 |
| net_avg_loss | -73.5438 |
| avg_hold_time_bars | 8.6094 |
| exposure | 0.1914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
