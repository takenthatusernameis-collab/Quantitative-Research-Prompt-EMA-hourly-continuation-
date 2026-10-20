# EMA Hourly Continuation — IOTX/USDT P89_200

**Symbol:** IOTX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.6282 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 0.9519 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -2.8433 |
| sortino_ratio | -0.8485 |
| max_drawdown | 0.6553 |
| cagr | -0.3327 |
| net_avg_win | 48.7601 |
| net_avg_loss | -75.9069 |
| avg_hold_time_bars | 10.9083 |
| exposure | 0.2216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
