# EMA Hourly Continuation — FLOW/USDT P50_144

**Symbol:** FLOW/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.5528 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.8539 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -4.1676 |
| sortino_ratio | -1.3184 |
| max_drawdown | 0.7972 |
| cagr | -0.4664 |
| net_avg_win | 43.4020 |
| net_avg_loss | -64.0554 |
| avg_hold_time_bars | 12.9205 |
| exposure | 0.2954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
