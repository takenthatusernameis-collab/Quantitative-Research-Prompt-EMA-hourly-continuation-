# EMA Hourly Continuation — DOGE/USDT P50_55

**Symbol:** DOGE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 817 |
| net_profit_factor | 0.1934 |
| net_win_rate | 0.3207 |
| gross_profit_factor | 0.7514 |
| gross_win_rate | 0.4039 |
| sharpe_ratio | -13.9441 |
| sortino_ratio | -6.0396 |
| max_drawdown | 0.9998 |
| cagr | -0.9661 |
| net_avg_win | 9.1514 |
| net_avg_loss | -22.3345 |
| avg_hold_time_bars | 1.7723 |
| exposure | 0.0658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
