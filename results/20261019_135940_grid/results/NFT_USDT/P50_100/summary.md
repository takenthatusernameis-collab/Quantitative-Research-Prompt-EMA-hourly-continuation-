# EMA Hourly Continuation — NFT/USDT P50_100

**Symbol:** NFT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1191 |
| net_profit_factor | 0.1897 |
| net_win_rate | 0.2191 |
| gross_profit_factor | 0.5809 |
| gross_win_rate | 0.2737 |
| sharpe_ratio | -20.1264 |
| sortino_ratio | -10.8534 |
| max_drawdown | 1.0000 |
| cagr | -0.9973 |
| net_avg_win | 8.9687 |
| net_avg_loss | -13.2697 |
| avg_hold_time_bars | 4.0949 |
| exposure | 0.2217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
