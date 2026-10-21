# EMA Hourly Continuation — SATS/USDT P21_100

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7689 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9470 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -1.9369 |
| sortino_ratio | -0.5959 |
| max_drawdown | 0.5591 |
| cagr | -0.2408 |
| net_avg_win | 73.7410 |
| net_avg_loss | -89.1926 |
| avg_hold_time_bars | 18.2260 |
| exposure | 0.3868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
