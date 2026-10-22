# EMA Hourly Continuation — CELR/USDT P21_34

**Symbol:** CELR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.6227 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -3.1183 |
| sortino_ratio | -0.9717 |
| max_drawdown | 0.6913 |
| cagr | -0.3586 |
| net_avg_win | 48.7727 |
| net_avg_loss | -72.5954 |
| avg_hold_time_bars | 5.0781 |
| exposure | 0.1089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
