# EMA Hourly Continuation — BTC/USDT P20_50

**Symbol:** BTC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.5395 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -4.2518 |
| sortino_ratio | -1.2851 |
| max_drawdown | 0.8136 |
| cagr | -0.4449 |
| net_avg_win | 40.0516 |
| net_avg_loss | -67.9542 |
| avg_hold_time_bars | 9.2671 |
| exposure | 0.1846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
