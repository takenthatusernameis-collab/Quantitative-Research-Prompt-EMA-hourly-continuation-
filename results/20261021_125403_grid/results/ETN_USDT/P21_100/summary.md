# EMA Hourly Continuation — ETN/USDT P21_100

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.5914 |
| net_win_rate | 0.4190 |
| gross_profit_factor | 0.7302 |
| gross_win_rate | 0.4190 |
| sharpe_ratio | -3.6630 |
| sortino_ratio | -1.1142 |
| max_drawdown | 0.6700 |
| cagr | -0.4028 |
| net_avg_win | 58.7484 |
| net_avg_loss | -71.6411 |
| avg_hold_time_bars | 16.3625 |
| exposure | 0.3457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
