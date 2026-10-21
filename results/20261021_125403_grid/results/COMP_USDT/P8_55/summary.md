# EMA Hourly Continuation — COMP/USDT P8_55

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.6844 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9083 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -2.9362 |
| sortino_ratio | -1.1130 |
| max_drawdown | 0.7454 |
| cagr | -0.3999 |
| net_avg_win | 45.8165 |
| net_avg_loss | -63.2459 |
| avg_hold_time_bars | 15.5526 |
| exposure | 0.4977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
