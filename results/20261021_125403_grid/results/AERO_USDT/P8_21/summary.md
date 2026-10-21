# EMA Hourly Continuation — AERO/USDT P8_21

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.8269 |
| net_win_rate | 0.5250 |
| gross_profit_factor | 1.0879 |
| gross_win_rate | 0.5250 |
| sharpe_ratio | -1.3226 |
| sortino_ratio | -0.4430 |
| max_drawdown | 0.4648 |
| cagr | -0.1856 |
| net_avg_win | 67.7414 |
| net_avg_loss | -90.5339 |
| avg_hold_time_bars | 5.6248 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
