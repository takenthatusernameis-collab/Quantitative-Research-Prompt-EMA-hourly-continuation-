# EMA Hourly Continuation — ANKR/USDT P26_144

**Symbol:** ANKR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.5677 |
| net_win_rate | 0.4277 |
| gross_profit_factor | 0.8432 |
| gross_win_rate | 0.4396 |
| sharpe_ratio | -4.6137 |
| sortino_ratio | -1.4557 |
| max_drawdown | 0.8327 |
| cagr | -0.5062 |
| net_avg_win | 50.4732 |
| net_avg_loss | -66.4453 |
| avg_hold_time_bars | 22.0059 |
| exposure | 0.5051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
