# EMA Hourly Continuation — HNT/USDT P20_100

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.7641 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9187 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -1.5988 |
| sortino_ratio | -0.4886 |
| max_drawdown | 0.4827 |
| cagr | -0.2028 |
| net_avg_win | 62.7889 |
| net_avg_loss | -78.3222 |
| avg_hold_time_bars | 19.0610 |
| exposure | 0.3977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
