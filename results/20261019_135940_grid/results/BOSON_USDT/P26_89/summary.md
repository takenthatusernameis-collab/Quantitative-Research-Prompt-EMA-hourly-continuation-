# EMA Hourly Continuation — BOSON/USDT P26_89

**Symbol:** BOSON/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.6624 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.9334 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -3.8534 |
| sortino_ratio | -1.4265 |
| max_drawdown | 0.8186 |
| cagr | -0.4904 |
| net_avg_win | 50.3461 |
| net_avg_loss | -64.7994 |
| avg_hold_time_bars | 9.8032 |
| exposure | 0.3079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
