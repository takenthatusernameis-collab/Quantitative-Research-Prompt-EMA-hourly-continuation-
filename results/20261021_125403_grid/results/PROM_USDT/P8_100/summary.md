# EMA Hourly Continuation — PROM/USDT P8_100

**Symbol:** PROM/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.6024 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 0.7918 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -3.9709 |
| sortino_ratio | -1.3478 |
| max_drawdown | 0.7954 |
| cagr | -0.4644 |
| net_avg_win | 48.1536 |
| net_avg_loss | -60.6875 |
| avg_hold_time_bars | 23.5061 |
| exposure | 0.6165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
