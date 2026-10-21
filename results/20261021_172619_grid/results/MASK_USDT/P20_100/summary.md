# EMA Hourly Continuation — MASK/USDT P20_100

**Symbol:** MASK/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.5823 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.7968 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -3.7221 |
| sortino_ratio | -1.1951 |
| max_drawdown | 0.7647 |
| cagr | -0.4257 |
| net_avg_win | 45.7563 |
| net_avg_loss | -63.3612 |
| avg_hold_time_bars | 18.9493 |
| exposure | 0.4419 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
