# EMA Hourly Continuation — LINK/USDT P8_100

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.8304 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0219 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.2327 |
| sortino_ratio | -0.3724 |
| max_drawdown | 0.4129 |
| cagr | -0.1596 |
| net_avg_win | 76.9865 |
| net_avg_loss | -95.2475 |
| avg_hold_time_bars | 32.3468 |
| exposure | 0.6528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
