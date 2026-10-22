# EMA Hourly Continuation — IOTX/USDT P8_26

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.7171 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 0.9968 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -2.5969 |
| sortino_ratio | -0.9797 |
| max_drawdown | 0.6781 |
| cagr | -0.3607 |
| net_avg_win | 49.1424 |
| net_avg_loss | -69.9410 |
| avg_hold_time_bars | 6.9608 |
| exposure | 0.2180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
