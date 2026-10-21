# EMA Hourly Continuation — NFT/USDT P50_55

**Symbol:** NFT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 172 |
| net_profit_factor | 0.1323 |
| net_win_rate | 0.1919 |
| gross_profit_factor | 0.3010 |
| gross_win_rate | 0.2035 |
| sharpe_ratio | -7.1110 |
| sortino_ratio | -1.4233 |
| max_drawdown | 0.8244 |
| cagr | -0.4985 |
| net_avg_win | 38.0279 |
| net_avg_loss | -68.2568 |
| avg_hold_time_bars | 8.2965 |
| exposure | 0.0649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
