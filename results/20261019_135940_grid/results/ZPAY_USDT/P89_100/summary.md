# EMA Hourly Continuation — ZPAY/USDT P89_100

**Symbol:** ZPAY/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.2796 |
| net_win_rate | 0.3350 |
| gross_profit_factor | 0.5454 |
| gross_win_rate | 0.3581 |
| sharpe_ratio | -8.0943 |
| sortino_ratio | -2.7994 |
| max_drawdown | 0.9684 |
| cagr | -0.7442 |
| net_avg_win | 18.5052 |
| net_avg_loss | -33.3389 |
| avg_hold_time_bars | 7.5957 |
| exposure | 0.2083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
