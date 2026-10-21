# EMA Hourly Continuation — TAIKO/USDT P144_200

**Symbol:** TAIKO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 189 |
| net_profit_factor | 0.6566 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9465 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.8335 |
| sortino_ratio | -0.3719 |
| max_drawdown | 0.3455 |
| cagr | -0.1558 |
| net_avg_win | 68.8456 |
| net_avg_loss | -99.4508 |
| avg_hold_time_bars | 6.4709 |
| exposure | 0.0587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
