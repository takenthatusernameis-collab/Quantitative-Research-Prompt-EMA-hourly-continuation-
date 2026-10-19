# EMA Hourly Continuation — NFT/USDT P21_144

**Symbol:** NFT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 994 |
| net_profit_factor | 0.3086 |
| net_win_rate | 0.2495 |
| gross_profit_factor | 0.6906 |
| gross_win_rate | 0.2797 |
| sharpe_ratio | -16.5573 |
| sortino_ratio | -7.8475 |
| max_drawdown | 1.0000 |
| cagr | -0.9858 |
| net_avg_win | 17.9980 |
| net_avg_loss | -19.3878 |
| avg_hold_time_bars | 10.9738 |
| exposure | 0.4958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
