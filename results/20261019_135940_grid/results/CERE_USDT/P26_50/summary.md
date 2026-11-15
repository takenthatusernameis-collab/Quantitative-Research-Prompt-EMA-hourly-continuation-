# EMA Hourly Continuation — CERE/USDT P26_50

**Symbol:** CERE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 980 |
| net_profit_factor | 0.3556 |
| net_win_rate | 0.3122 |
| gross_profit_factor | 0.7389 |
| gross_win_rate | 0.3633 |
| sharpe_ratio | -13.5387 |
| sortino_ratio | -6.1153 |
| max_drawdown | 0.9997 |
| cagr | -0.9623 |
| net_avg_win | 18.0281 |
| net_avg_loss | -23.0177 |
| avg_hold_time_bars | 5.4398 |
| exposure | 0.2423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
