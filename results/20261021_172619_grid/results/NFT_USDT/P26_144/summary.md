# EMA Hourly Continuation — NFT/USDT P26_144

**Symbol:** NFT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.4046 |
| net_win_rate | 0.3366 |
| gross_profit_factor | 0.6414 |
| gross_win_rate | 0.3390 |
| sharpe_ratio | -6.9085 |
| sortino_ratio | -2.0226 |
| max_drawdown | 0.9116 |
| cagr | -0.6141 |
| net_avg_win | 44.4185 |
| net_avg_loss | -55.6889 |
| avg_hold_time_bars | 22.7579 |
| exposure | 0.4272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
