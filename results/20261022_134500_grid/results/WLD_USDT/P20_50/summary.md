# EMA Hourly Continuation — WLD/USDT P20_50

**Symbol:** WLD/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.5677 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9195 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -5.2690 |
| sortino_ratio | -2.2397 |
| max_drawdown | 0.9381 |
| cagr | -0.6668 |
| net_avg_win | 27.7698 |
| net_avg_loss | -45.0505 |
| avg_hold_time_bars | 5.6245 |
| exposure | 0.2362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
