# EMA Hourly Continuation — RENDER/USDT P20_34

**Symbol:** RENDER/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 986 |
| net_profit_factor | 0.3602 |
| net_win_rate | 0.4118 |
| gross_profit_factor | 0.7241 |
| gross_win_rate | 0.4320 |
| sharpe_ratio | -10.5427 |
| sortino_ratio | -5.0479 |
| max_drawdown | 0.9962 |
| cagr | -0.9233 |
| net_avg_win | 13.8123 |
| net_avg_loss | -26.8433 |
| avg_hold_time_bars | 2.6957 |
| exposure | 0.1403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
