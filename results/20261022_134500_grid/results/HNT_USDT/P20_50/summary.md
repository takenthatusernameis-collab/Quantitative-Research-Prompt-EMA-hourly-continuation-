# EMA Hourly Continuation — HNT/USDT P20_50

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1048 |
| net_profit_factor | 0.4970 |
| net_win_rate | 0.4408 |
| gross_profit_factor | 0.8207 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -7.4074 |
| sortino_ratio | -3.3857 |
| max_drawdown | 0.9843 |
| cagr | -0.8056 |
| net_avg_win | 21.0409 |
| net_avg_loss | -33.3744 |
| avg_hold_time_bars | 4.6450 |
| exposure | 0.2213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
