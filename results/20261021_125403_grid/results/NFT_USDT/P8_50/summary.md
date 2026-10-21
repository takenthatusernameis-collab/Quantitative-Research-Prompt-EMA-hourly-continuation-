# EMA Hourly Continuation — NFT/USDT P8_50

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.4023 |
| net_win_rate | 0.3208 |
| gross_profit_factor | 0.6736 |
| gross_win_rate | 0.3306 |
| sharpe_ratio | -9.3263 |
| sortino_ratio | -3.3531 |
| max_drawdown | 0.9827 |
| cagr | -0.7995 |
| net_avg_win | 33.5681 |
| net_avg_loss | -39.4150 |
| avg_hold_time_bars | 13.8388 |
| exposure | 0.3862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
