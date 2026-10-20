# EMA Hourly Continuation — ELON/USDT P50_144

**Symbol:** ELON/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.4245 |
| net_win_rate | 0.4197 |
| gross_profit_factor | 0.6726 |
| gross_win_rate | 0.4236 |
| sharpe_ratio | -5.1655 |
| sortino_ratio | -1.6636 |
| max_drawdown | 0.8621 |
| cagr | -0.5415 |
| net_avg_win | 29.1998 |
| net_avg_loss | -49.7511 |
| avg_hold_time_bars | 10.8066 |
| exposure | 0.2540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
