# EMA Hourly Continuation — ETH/USDT P55_100

**Symbol:** ETH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.6493 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0099 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -2.2271 |
| sortino_ratio | -0.5453 |
| max_drawdown | 0.4967 |
| cagr | -0.2207 |
| net_avg_win | 59.4311 |
| net_avg_loss | -92.1632 |
| avg_hold_time_bars | 8.3149 |
| exposure | 0.1092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
