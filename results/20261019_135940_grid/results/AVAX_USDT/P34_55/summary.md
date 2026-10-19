# EMA Hourly Continuation — AVAX/USDT P34_55

**Symbol:** AVAX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 854 |
| net_profit_factor | 0.4093 |
| net_win_rate | 0.4297 |
| gross_profit_factor | 0.8617 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -8.9354 |
| sortino_ratio | -3.7072 |
| max_drawdown | 0.9917 |
| cagr | -0.8489 |
| net_avg_win | 18.7191 |
| net_avg_loss | -34.4621 |
| avg_hold_time_bars | 2.8864 |
| exposure | 0.1120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
