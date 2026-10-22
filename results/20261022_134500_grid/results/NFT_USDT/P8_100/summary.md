# EMA Hourly Continuation — NFT/USDT P8_100

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1257 |
| net_profit_factor | 0.2864 |
| net_win_rate | 0.2673 |
| gross_profit_factor | 0.6917 |
| gross_win_rate | 0.3023 |
| sharpe_ratio | -18.2149 |
| sortino_ratio | -9.6379 |
| max_drawdown | 1.0000 |
| cagr | -0.9948 |
| net_avg_win | 11.9432 |
| net_avg_loss | -15.2149 |
| avg_hold_time_bars | 10.1846 |
| exposure | 0.5819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
