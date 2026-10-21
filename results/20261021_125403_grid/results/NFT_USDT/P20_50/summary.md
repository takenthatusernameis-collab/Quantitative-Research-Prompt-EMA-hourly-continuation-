# EMA Hourly Continuation — NFT/USDT P20_50

**Symbol:** NFT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.3146 |
| net_win_rate | 0.2917 |
| gross_profit_factor | 0.5862 |
| gross_win_rate | 0.3079 |
| sharpe_ratio | -8.7440 |
| sortino_ratio | -2.6754 |
| max_drawdown | 0.9603 |
| cagr | -0.7232 |
| net_avg_win | 34.9789 |
| net_avg_loss | -45.7841 |
| avg_hold_time_bars | 9.4630 |
| exposure | 0.1858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
