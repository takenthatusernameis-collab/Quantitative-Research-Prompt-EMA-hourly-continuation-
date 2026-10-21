# EMA Hourly Continuation — NFT/USDT P12_20

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.2566 |
| net_win_rate | 0.2440 |
| gross_profit_factor | 0.5195 |
| gross_win_rate | 0.2474 |
| sharpe_ratio | -8.4027 |
| sortino_ratio | -2.1578 |
| max_drawdown | 0.9314 |
| cagr | -0.6550 |
| net_avg_win | 45.2667 |
| net_avg_loss | -56.9242 |
| avg_hold_time_bars | 5.8557 |
| exposure | 0.0775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
