# EMA Hourly Continuation — BCH/USDT P20_100

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5794 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.9852 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -4.6727 |
| sortino_ratio | -1.6691 |
| max_drawdown | 0.8764 |
| cagr | -0.5470 |
| net_avg_win | 39.5056 |
| net_avg_loss | -61.2608 |
| avg_hold_time_bars | 15.0959 |
| exposure | 0.4364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
