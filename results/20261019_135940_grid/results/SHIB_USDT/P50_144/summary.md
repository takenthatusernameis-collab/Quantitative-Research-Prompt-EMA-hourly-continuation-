# EMA Hourly Continuation — SHIB/USDT P50_144

**Symbol:** SHIB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.5597 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.9330 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -4.2981 |
| sortino_ratio | -1.3536 |
| max_drawdown | 0.8189 |
| cagr | -0.4868 |
| net_avg_win | 43.2308 |
| net_avg_loss | -68.3686 |
| avg_hold_time_bars | 11.3458 |
| exposure | 0.2625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
