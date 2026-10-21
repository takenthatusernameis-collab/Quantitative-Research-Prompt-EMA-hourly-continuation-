# EMA Hourly Continuation — DEEP/USDT P12_100

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.9457 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0878 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -0.3320 |
| sortino_ratio | -0.0991 |
| max_drawdown | 0.2881 |
| cagr | -0.0508 |
| net_avg_win | 95.9615 |
| net_avg_loss | -111.3120 |
| avg_hold_time_bars | 29.7486 |
| exposure | 0.5828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
