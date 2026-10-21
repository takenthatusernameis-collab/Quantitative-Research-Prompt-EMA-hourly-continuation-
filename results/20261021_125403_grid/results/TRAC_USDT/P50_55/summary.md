# EMA Hourly Continuation — TRAC/USDT P50_55

**Symbol:** TRAC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 155 |
| net_profit_factor | 0.7258 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 0.9998 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -1.1804 |
| sortino_ratio | -0.2110 |
| max_drawdown | 0.2677 |
| cagr | -0.0914 |
| net_avg_win | 72.5976 |
| net_avg_loss | -101.3203 |
| avg_hold_time_bars | 8.5871 |
| exposure | 0.0605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
