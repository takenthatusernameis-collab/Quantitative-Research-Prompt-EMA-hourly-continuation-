# EMA Hourly Continuation — NFT/USDT P20_100

**Symbol:** NFT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.4602 |
| net_win_rate | 0.3785 |
| gross_profit_factor | 0.7740 |
| gross_win_rate | 0.3785 |
| sharpe_ratio | -6.7436 |
| sortino_ratio | -2.1022 |
| max_drawdown | 0.9201 |
| cagr | -0.6278 |
| net_avg_win | 44.3958 |
| net_avg_loss | -58.7467 |
| avg_hold_time_bars | 18.0194 |
| exposure | 0.3809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
