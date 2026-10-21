# EMA Hourly Continuation — NFT/USDT P55_100

**Symbol:** NFT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.3597 |
| net_win_rate | 0.3353 |
| gross_profit_factor | 0.7406 |
| gross_win_rate | 0.3441 |
| sharpe_ratio | -7.0982 |
| sortino_ratio | -1.9162 |
| max_drawdown | 0.8997 |
| cagr | -0.5961 |
| net_avg_win | 44.2277 |
| net_avg_loss | -62.0171 |
| avg_hold_time_bars | 8.9647 |
| exposure | 0.1385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
