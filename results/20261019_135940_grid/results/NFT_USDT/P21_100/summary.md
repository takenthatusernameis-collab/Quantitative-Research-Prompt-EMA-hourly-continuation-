# EMA Hourly Continuation — NFT/USDT P21_100

**Symbol:** NFT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1183 |
| net_profit_factor | 0.3126 |
| net_win_rate | 0.2502 |
| gross_profit_factor | 0.7327 |
| gross_win_rate | 0.2891 |
| sharpe_ratio | -18.4479 |
| sortino_ratio | -9.5987 |
| max_drawdown | 1.0000 |
| cagr | -0.9947 |
| net_avg_win | 15.3612 |
| net_avg_loss | -16.4001 |
| avg_hold_time_bars | 7.6982 |
| exposure | 0.4140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
