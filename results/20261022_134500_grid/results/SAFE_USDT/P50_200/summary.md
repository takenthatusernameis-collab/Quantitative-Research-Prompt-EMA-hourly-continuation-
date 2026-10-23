# EMA Hourly Continuation — SAFE/USDT P50_200

**Symbol:** SAFE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.7374 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0407 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.9356 |
| sortino_ratio | -0.5344 |
| max_drawdown | 0.4872 |
| cagr | -0.2231 |
| net_avg_win | 69.3849 |
| net_avg_loss | -94.5980 |
| avg_hold_time_bars | 23.7984 |
| exposure | 0.4109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
