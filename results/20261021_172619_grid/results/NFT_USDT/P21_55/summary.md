# EMA Hourly Continuation — NFT/USDT P21_55

**Symbol:** NFT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.3381 |
| net_win_rate | 0.3143 |
| gross_profit_factor | 0.6240 |
| gross_win_rate | 0.3209 |
| sharpe_ratio | -8.6283 |
| sortino_ratio | -2.7019 |
| max_drawdown | 0.9611 |
| cagr | -0.7254 |
| net_avg_win | 34.3319 |
| net_avg_loss | -46.5389 |
| avg_hold_time_bars | 9.7429 |
| exposure | 0.2015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
