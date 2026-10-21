# EMA Hourly Continuation — DASH/USDT P50_200

**Symbol:** DASH/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.6694 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8511 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -1.9815 |
| sortino_ratio | -0.4835 |
| max_drawdown | 0.4671 |
| cagr | -0.1994 |
| net_avg_win | 63.2350 |
| net_avg_loss | -82.4366 |
| avg_hold_time_bars | 26.4456 |
| exposure | 0.3534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
