# EMA Hourly Continuation — AUCTION/USDT P21_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.5753 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8729 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -4.7119 |
| sortino_ratio | -1.6993 |
| max_drawdown | 0.8760 |
| cagr | -0.5553 |
| net_avg_win | 39.4364 |
| net_avg_loss | -56.9344 |
| avg_hold_time_bars | 14.3263 |
| exposure | 0.4273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
