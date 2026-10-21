# EMA Hourly Continuation — NFT/USDT P8_12

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.2239 |
| net_win_rate | 0.2247 |
| gross_profit_factor | 0.4399 |
| gross_win_rate | 0.2285 |
| sharpe_ratio | -8.2700 |
| sortino_ratio | -2.0415 |
| max_drawdown | 0.9179 |
| cagr | -0.6291 |
| net_avg_win | 44.0965 |
| net_avg_loss | -57.0874 |
| avg_hold_time_bars | 4.3296 |
| exposure | 0.0525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
