# EMA Hourly Continuation — HNT/USDT P50_200

**Symbol:** HNT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5404 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.7132 |
| gross_win_rate | 0.4279 |
| sharpe_ratio | -3.7733 |
| sortino_ratio | -1.1086 |
| max_drawdown | 0.7394 |
| cagr | -0.4077 |
| net_avg_win | 46.0090 |
| net_avg_loss | -63.6782 |
| avg_hold_time_bars | 20.4256 |
| exposure | 0.4057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
