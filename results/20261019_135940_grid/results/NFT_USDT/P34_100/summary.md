# EMA Hourly Continuation — NFT/USDT P34_100

**Symbol:** NFT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1155 |
| net_profit_factor | 0.2723 |
| net_win_rate | 0.2364 |
| gross_profit_factor | 0.6827 |
| gross_win_rate | 0.2745 |
| sharpe_ratio | -18.9878 |
| sortino_ratio | -9.8842 |
| max_drawdown | 1.0000 |
| cagr | -0.9957 |
| net_avg_win | 13.7076 |
| net_avg_loss | -15.5807 |
| avg_hold_time_bars | 6.5697 |
| exposure | 0.3449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
