# EMA Hourly Continuation — HNT/USDT P26_200

**Symbol:** HNT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.6664 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.8856 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -2.4331 |
| sortino_ratio | -0.6613 |
| max_drawdown | 0.5987 |
| cagr | -0.2729 |
| net_avg_win | 61.4722 |
| net_avg_loss | -82.9767 |
| avg_hold_time_bars | 34.9074 |
| exposure | 0.5998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
