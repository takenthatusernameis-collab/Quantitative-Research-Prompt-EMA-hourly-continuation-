# EMA Hourly Continuation — VET/USDT P8_100

**Symbol:** VET/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.9063 |
| net_win_rate | 0.5336 |
| gross_profit_factor | 1.1365 |
| gross_win_rate | 0.5336 |
| sharpe_ratio | -0.6407 |
| sortino_ratio | -0.2048 |
| max_drawdown | 0.3459 |
| cagr | -0.0949 |
| net_avg_win | 81.7999 |
| net_avg_loss | -103.2610 |
| avg_hold_time_bars | 27.9063 |
| exposure | 0.6228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
