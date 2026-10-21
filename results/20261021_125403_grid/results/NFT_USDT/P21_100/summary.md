# EMA Hourly Continuation — NFT/USDT P21_100

**Symbol:** NFT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.4589 |
| net_win_rate | 0.3737 |
| gross_profit_factor | 0.7685 |
| gross_win_rate | 0.3737 |
| sharpe_ratio | -6.8379 |
| sortino_ratio | -2.1275 |
| max_drawdown | 0.9229 |
| cagr | -0.6324 |
| net_avg_win | 45.0510 |
| net_avg_loss | -58.5650 |
| avg_hold_time_bars | 17.8121 |
| exposure | 0.3749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
