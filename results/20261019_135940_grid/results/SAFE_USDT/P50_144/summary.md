# EMA Hourly Continuation — SAFE/USDT P50_144

**Symbol:** SAFE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6654 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9636 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -2.6441 |
| sortino_ratio | -0.8172 |
| max_drawdown | 0.6359 |
| cagr | -0.3202 |
| net_avg_win | 52.9567 |
| net_avg_loss | -76.9361 |
| avg_hold_time_bars | 14.1335 |
| exposure | 0.3055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
