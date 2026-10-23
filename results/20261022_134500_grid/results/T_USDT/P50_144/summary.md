# EMA Hourly Continuation — T/USDT P50_144

**Symbol:** T/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.5688 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -3.8363 |
| sortino_ratio | -1.1461 |
| max_drawdown | 0.7515 |
| cagr | -0.4224 |
| net_avg_win | 47.5295 |
| net_avg_loss | -71.5291 |
| avg_hold_time_bars | 14.1486 |
| exposure | 0.2888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
