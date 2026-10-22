# EMA Hourly Continuation — NFT/USDT P26_50

**Symbol:** NFT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1538 |
| net_profit_factor | 0.1525 |
| net_win_rate | 0.1853 |
| gross_profit_factor | 0.5445 |
| gross_win_rate | 0.2620 |
| sharpe_ratio | -24.6124 |
| sortino_ratio | -15.4160 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 6.3138 |
| net_avg_loss | -9.4170 |
| avg_hold_time_bars | 3.3778 |
| exposure | 0.2361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
