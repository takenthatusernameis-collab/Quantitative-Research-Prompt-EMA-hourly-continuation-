# EMA Hourly Continuation — CELR/USDT P34_100

**Symbol:** CELR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.5722 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8750 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -4.2365 |
| sortino_ratio | -1.5233 |
| max_drawdown | 0.8430 |
| cagr | -0.5181 |
| net_avg_win | 36.5399 |
| net_avg_loss | -56.5184 |
| avg_hold_time_bars | 9.6357 |
| exposure | 0.2860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
