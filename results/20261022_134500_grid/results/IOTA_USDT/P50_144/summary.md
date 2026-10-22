# EMA Hourly Continuation — IOTA/USDT P50_144

**Symbol:** IOTA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.5937 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -3.6558 |
| sortino_ratio | -1.1327 |
| max_drawdown | 0.7557 |
| cagr | -0.4147 |
| net_avg_win | 48.8993 |
| net_avg_loss | -70.0080 |
| avg_hold_time_bars | 12.2765 |
| exposure | 0.2684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
