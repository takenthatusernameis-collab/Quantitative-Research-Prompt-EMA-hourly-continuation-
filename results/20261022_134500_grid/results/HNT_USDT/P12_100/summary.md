# EMA Hourly Continuation — HNT/USDT P12_100

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.5546 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.7771 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -4.8224 |
| sortino_ratio | -1.8359 |
| max_drawdown | 0.8934 |
| cagr | -0.5850 |
| net_avg_win | 33.8939 |
| net_avg_loss | -49.1034 |
| avg_hold_time_bars | 16.4782 |
| exposure | 0.5498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
