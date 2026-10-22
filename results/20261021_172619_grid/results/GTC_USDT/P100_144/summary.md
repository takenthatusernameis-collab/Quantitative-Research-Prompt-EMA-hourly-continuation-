# EMA Hourly Continuation — GTC/USDT P100_144

**Symbol:** GTC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.6223 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.8645 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -2.4438 |
| sortino_ratio | -0.5863 |
| max_drawdown | 0.5258 |
| cagr | -0.2353 |
| net_avg_win | 61.1718 |
| net_avg_loss | -85.9360 |
| avg_hold_time_bars | 6.7279 |
| exposure | 0.0865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
