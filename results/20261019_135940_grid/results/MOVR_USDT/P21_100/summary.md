# EMA Hourly Continuation — MOVR/USDT P21_100

**Symbol:** MOVR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 764 |
| net_profit_factor | 0.5300 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.8002 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -5.3167 |
| sortino_ratio | -2.0545 |
| max_drawdown | 0.9181 |
| cagr | -0.6282 |
| net_avg_win | 30.9483 |
| net_avg_loss | -45.3560 |
| avg_hold_time_bars | 11.2238 |
| exposure | 0.3898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
