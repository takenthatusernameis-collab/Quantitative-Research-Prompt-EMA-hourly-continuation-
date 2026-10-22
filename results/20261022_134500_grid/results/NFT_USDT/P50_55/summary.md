# EMA Hourly Continuation — NFT/USDT P50_55

**Symbol:** NFT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1355 |
| net_profit_factor | 0.0489 |
| net_win_rate | 0.1151 |
| gross_profit_factor | 0.3494 |
| gross_win_rate | 0.2066 |
| sharpe_ratio | -26.2608 |
| sortino_ratio | -17.0396 |
| max_drawdown | 1.0000 |
| cagr | -0.9999 |
| net_avg_win | 3.2934 |
| net_avg_loss | -8.7688 |
| avg_hold_time_bars | 1.9815 |
| exposure | 0.1220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
