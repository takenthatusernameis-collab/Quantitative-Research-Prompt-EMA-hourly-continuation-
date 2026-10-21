# EMA Hourly Continuation — NFT/USDT P20_55

**Symbol:** NFT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.3491 |
| net_win_rate | 0.3218 |
| gross_profit_factor | 0.6479 |
| gross_win_rate | 0.3305 |
| sharpe_ratio | -8.4960 |
| sortino_ratio | -2.6800 |
| max_drawdown | 0.9599 |
| cagr | -0.7222 |
| net_avg_win | 34.5464 |
| net_avg_loss | -46.9633 |
| avg_hold_time_bars | 9.8164 |
| exposure | 0.2066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
