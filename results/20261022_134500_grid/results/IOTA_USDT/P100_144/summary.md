# EMA Hourly Continuation — IOTA/USDT P100_144

**Symbol:** IOTA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.4644 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8870 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -4.9543 |
| sortino_ratio | -1.5093 |
| max_drawdown | 0.8546 |
| cagr | -0.5266 |
| net_avg_win | 34.3264 |
| net_avg_loss | -62.0262 |
| avg_hold_time_bars | 4.5778 |
| exposure | 0.0976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
