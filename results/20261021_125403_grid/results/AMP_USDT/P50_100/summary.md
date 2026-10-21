# EMA Hourly Continuation — AMP/USDT P50_100

**Symbol:** AMP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.5950 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.8217 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -3.2366 |
| sortino_ratio | -0.9178 |
| max_drawdown | 0.6730 |
| cagr | -0.3440 |
| net_avg_win | 53.6179 |
| net_avg_loss | -74.3283 |
| avg_hold_time_bars | 9.9747 |
| exposure | 0.1795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
