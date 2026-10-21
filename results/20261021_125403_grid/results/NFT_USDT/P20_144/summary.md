# EMA Hourly Continuation — NFT/USDT P20_144

**Symbol:** NFT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.4144 |
| net_win_rate | 0.3443 |
| gross_profit_factor | 0.6599 |
| gross_win_rate | 0.3465 |
| sharpe_ratio | -7.1252 |
| sortino_ratio | -2.1911 |
| max_drawdown | 0.9267 |
| cagr | -0.6431 |
| net_avg_win | 41.6812 |
| net_avg_loss | -52.8161 |
| avg_hold_time_bars | 21.6864 |
| exposure | 0.4495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
