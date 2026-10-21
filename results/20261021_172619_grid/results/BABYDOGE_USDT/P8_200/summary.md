# EMA Hourly Continuation — BABYDOGE/USDT P8_200

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 75 |
| net_profit_factor | 0.8740 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9207 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -0.3594 |
| sortino_ratio | -0.0442 |
| max_drawdown | 0.1411 |
| cagr | -0.0209 |
| net_avg_win | 99.8952 |
| net_avg_loss | -105.5026 |
| avg_hold_time_bars | 143.8533 |
| exposure | 0.4882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
