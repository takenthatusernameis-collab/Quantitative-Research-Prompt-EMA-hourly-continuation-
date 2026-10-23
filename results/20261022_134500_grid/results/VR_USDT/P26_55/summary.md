# EMA Hourly Continuation — VR/USDT P26_55

**Symbol:** VR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1007 |
| net_profit_factor | 0.4109 |
| net_win_rate | 0.3138 |
| gross_profit_factor | 0.7098 |
| gross_win_rate | 0.3357 |
| sharpe_ratio | -14.1904 |
| sortino_ratio | -6.4399 |
| max_drawdown | 0.9999 |
| cagr | -0.9780 |
| net_avg_win | 22.0729 |
| net_avg_loss | -24.5649 |
| avg_hold_time_bars | 4.3366 |
| exposure | 0.1985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
