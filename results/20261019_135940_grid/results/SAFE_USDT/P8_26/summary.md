# EMA Hourly Continuation — SAFE/USDT P8_26

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1430 |
| net_profit_factor | 0.4463 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8666 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -8.7764 |
| sortino_ratio | -4.6813 |
| max_drawdown | 0.9969 |
| cagr | -0.9000 |
| net_avg_win | 12.3974 |
| net_avg_loss | -23.0195 |
| avg_hold_time_bars | 4.3881 |
| exposure | 0.2874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
