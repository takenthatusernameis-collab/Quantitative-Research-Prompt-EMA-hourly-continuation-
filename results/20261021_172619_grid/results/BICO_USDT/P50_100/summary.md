# EMA Hourly Continuation — BICO/USDT P50_100

**Symbol:** BICO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.6528 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8514 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -2.7376 |
| sortino_ratio | -0.8243 |
| max_drawdown | 0.6239 |
| cagr | -0.3154 |
| net_avg_win | 55.7537 |
| net_avg_loss | -73.6675 |
| avg_hold_time_bars | 10.4049 |
| exposure | 0.2114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
