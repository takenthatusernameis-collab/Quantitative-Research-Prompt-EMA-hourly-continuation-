# EMA Hourly Continuation — PROM/USDT P8_34

**Symbol:** PROM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 781 |
| net_profit_factor | 0.6454 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.9000 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -4.1226 |
| sortino_ratio | -1.6391 |
| max_drawdown | 0.8553 |
| cagr | -0.5320 |
| net_avg_win | 42.6963 |
| net_avg_loss | -57.4481 |
| avg_hold_time_bars | 9.7209 |
| exposure | 0.3451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
