# EMA Hourly Continuation — DASH/USDT P50_144

**Symbol:** DASH/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.4508 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8457 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -4.9510 |
| sortino_ratio | -1.6249 |
| max_drawdown | 0.8784 |
| cagr | -0.5519 |
| net_avg_win | 28.8108 |
| net_avg_loss | -52.2662 |
| avg_hold_time_bars | 9.3880 |
| exposure | 0.2343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
