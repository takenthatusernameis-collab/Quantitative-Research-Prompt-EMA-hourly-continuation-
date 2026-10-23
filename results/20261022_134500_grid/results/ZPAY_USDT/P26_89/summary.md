# EMA Hourly Continuation — ZPAY/USDT P26_89

**Symbol:** ZPAY/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.4809 |
| net_win_rate | 0.3523 |
| gross_profit_factor | 0.6339 |
| gross_win_rate | 0.3539 |
| sharpe_ratio | -6.3352 |
| sortino_ratio | -2.1662 |
| max_drawdown | 0.9268 |
| cagr | -0.6380 |
| net_avg_win | 40.5289 |
| net_avg_loss | -45.8276 |
| avg_hold_time_bars | 16.4908 |
| exposure | 0.4470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
