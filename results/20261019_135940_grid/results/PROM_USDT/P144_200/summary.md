# EMA Hourly Continuation — PROM/USDT P144_200

**Symbol:** PROM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.3029 |
| net_win_rate | 0.3555 |
| gross_profit_factor | 0.6864 |
| gross_win_rate | 0.4137 |
| sharpe_ratio | -7.4687 |
| sortino_ratio | -2.3321 |
| max_drawdown | 0.9497 |
| cagr | -0.6889 |
| net_avg_win | 24.0515 |
| net_avg_loss | -43.8072 |
| avg_hold_time_bars | 4.4366 |
| exposure | 0.0970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
