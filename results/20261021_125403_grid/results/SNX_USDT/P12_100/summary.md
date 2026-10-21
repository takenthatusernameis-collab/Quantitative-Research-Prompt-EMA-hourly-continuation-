# EMA Hourly Continuation — SNX/USDT P12_100

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.8343 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 1.0093 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -1.3691 |
| sortino_ratio | -0.4483 |
| max_drawdown | 0.4336 |
| cagr | -0.1884 |
| net_avg_win | 78.3569 |
| net_avg_loss | -94.2827 |
| avg_hold_time_bars | 22.0705 |
| exposure | 0.5243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
