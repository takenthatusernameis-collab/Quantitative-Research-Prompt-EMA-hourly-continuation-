# EMA Hourly Continuation — CELR/USDT P34_200

**Symbol:** CELR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.7542 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.9043 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -1.5848 |
| sortino_ratio | -0.4090 |
| max_drawdown | 0.4068 |
| cagr | -0.1722 |
| net_avg_win | 74.1176 |
| net_avg_loss | -89.1857 |
| avg_hold_time_bars | 35.7121 |
| exposure | 0.5333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
