# EMA Hourly Continuation — NFT/USDT P12_100

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1224 |
| net_profit_factor | 0.3322 |
| net_win_rate | 0.2590 |
| gross_profit_factor | 0.7832 |
| gross_win_rate | 0.2974 |
| sharpe_ratio | -18.2233 |
| sortino_ratio | -9.5445 |
| max_drawdown | 1.0000 |
| cagr | -0.9945 |
| net_avg_win | 15.6959 |
| net_avg_loss | -16.5111 |
| avg_hold_time_bars | 9.1422 |
| exposure | 0.5086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
