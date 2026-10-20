# EMA Hourly Continuation — DYDX/USDT P50_89

**Symbol:** DYDX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.5565 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -5.2040 |
| sortino_ratio | -1.9719 |
| max_drawdown | 0.9104 |
| cagr | -0.6141 |
| net_avg_win | 33.2358 |
| net_avg_loss | -54.0489 |
| avg_hold_time_bars | 4.3435 |
| exposure | 0.1425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
