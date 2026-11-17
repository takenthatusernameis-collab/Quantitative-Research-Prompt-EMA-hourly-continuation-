# EMA Hourly Continuation — NUM/USDT P20_100

**Symbol:** NUM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.5341 |
| net_win_rate | 0.3948 |
| gross_profit_factor | 0.7543 |
| gross_win_rate | 0.3977 |
| sharpe_ratio | -6.0818 |
| sortino_ratio | -2.2532 |
| max_drawdown | 0.9337 |
| cagr | -0.6550 |
| net_avg_win | 38.9413 |
| net_avg_loss | -47.5696 |
| avg_hold_time_bars | 13.2507 |
| exposure | 0.4180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
