# EMA Hourly Continuation — SUN/USDT P12_100

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.5794 |
| net_win_rate | 0.4456 |
| gross_profit_factor | 0.9351 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -4.6560 |
| sortino_ratio | -1.4238 |
| max_drawdown | 0.8299 |
| cagr | -0.4942 |
| net_avg_win | 54.1051 |
| net_avg_loss | -75.0614 |
| avg_hold_time_bars | 26.8486 |
| exposure | 0.5698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
