# EMA Hourly Continuation — NFT/USDT P26_100

**Symbol:** NFT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1161 |
| net_profit_factor | 0.3016 |
| net_win_rate | 0.2524 |
| gross_profit_factor | 0.7050 |
| gross_win_rate | 0.2860 |
| sharpe_ratio | -18.3640 |
| sortino_ratio | -9.4944 |
| max_drawdown | 1.0000 |
| cagr | -0.9944 |
| net_avg_win | 14.7394 |
| net_avg_loss | -16.4961 |
| avg_hold_time_bars | 7.2730 |
| exposure | 0.3838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
