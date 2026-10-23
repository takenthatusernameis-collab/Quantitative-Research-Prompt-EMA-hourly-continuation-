# EMA Hourly Continuation — CELR/USDT P34_144

**Symbol:** CELR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.6135 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8647 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -3.4358 |
| sortino_ratio | -1.0854 |
| max_drawdown | 0.7322 |
| cagr | -0.3997 |
| net_avg_win | 49.7455 |
| net_avg_loss | -68.8648 |
| avg_hold_time_bars | 17.8410 |
| exposure | 0.4061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
