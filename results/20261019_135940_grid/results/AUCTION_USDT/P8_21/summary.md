# EMA Hourly Continuation — AUCTION/USDT P8_21

**Symbol:** AUCTION/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1465 |
| net_profit_factor | 0.4414 |
| net_win_rate | 0.4089 |
| gross_profit_factor | 0.8390 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -11.4820 |
| sortino_ratio | -6.1996 |
| max_drawdown | 0.9996 |
| cagr | -0.9554 |
| net_avg_win | 13.1849 |
| net_avg_loss | -20.6627 |
| avg_hold_time_bars | 4.2034 |
| exposure | 0.2787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
