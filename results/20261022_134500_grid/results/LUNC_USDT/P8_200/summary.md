# EMA Hourly Continuation — LUNC/USDT P8_200

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.5345 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8189 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -3.9855 |
| sortino_ratio | -1.2448 |
| max_drawdown | 0.7885 |
| cagr | -0.4479 |
| net_avg_win | 39.7246 |
| net_avg_loss | -62.1210 |
| avg_hold_time_bars | 34.6829 |
| exposure | 0.7756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
