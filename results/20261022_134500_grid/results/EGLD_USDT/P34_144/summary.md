# EMA Hourly Continuation — EGLD/USDT P34_144

**Symbol:** EGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6148 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9701 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -2.8858 |
| sortino_ratio | -0.8790 |
| max_drawdown | 0.6633 |
| cagr | -0.3432 |
| net_avg_win | 45.0509 |
| net_avg_loss | -71.4254 |
| avg_hold_time_bars | 19.1004 |
| exposure | 0.4063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
