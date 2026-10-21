# EMA Hourly Continuation — NFT/USDT P8_100

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.4946 |
| net_win_rate | 0.3811 |
| gross_profit_factor | 0.7975 |
| gross_win_rate | 0.3829 |
| sharpe_ratio | -6.9299 |
| sortino_ratio | -2.3373 |
| max_drawdown | 0.9376 |
| cagr | -0.6666 |
| net_avg_win | 43.6395 |
| net_avg_loss | -54.3408 |
| avg_hold_time_bars | 20.7623 |
| exposure | 0.5200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
