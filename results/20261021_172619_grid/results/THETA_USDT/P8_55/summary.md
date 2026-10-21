# EMA Hourly Continuation — THETA/USDT P8_55

**Symbol:** THETA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.7896 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9802 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -1.8790 |
| sortino_ratio | -0.6843 |
| max_drawdown | 0.5693 |
| cagr | -0.2706 |
| net_avg_win | 63.9681 |
| net_avg_loss | -79.7713 |
| avg_hold_time_bars | 15.4328 |
| exposure | 0.4539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
