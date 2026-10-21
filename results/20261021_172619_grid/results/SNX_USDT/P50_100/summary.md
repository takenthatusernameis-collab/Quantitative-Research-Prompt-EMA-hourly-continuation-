# EMA Hourly Continuation — SNX/USDT P50_100

**Symbol:** SNX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.9619 |
| net_win_rate | 0.5590 |
| gross_profit_factor | 1.2627 |
| gross_win_rate | 0.5590 |
| sharpe_ratio | -0.2053 |
| sortino_ratio | -0.0589 |
| max_drawdown | 0.2851 |
| cagr | -0.0327 |
| net_avg_win | 93.3269 |
| net_avg_loss | -122.9662 |
| avg_hold_time_bars | 8.5436 |
| exposure | 0.1508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
