# EMA Hourly Continuation — BRETT/USDT P21_55

**Symbol:** BRETT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 897 |
| net_profit_factor | 0.5819 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -6.1582 |
| sortino_ratio | -2.6587 |
| max_drawdown | 0.9540 |
| cagr | -0.7256 |
| net_avg_win | 33.5056 |
| net_avg_loss | -45.5153 |
| avg_hold_time_bars | 5.1828 |
| exposure | 0.2237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
