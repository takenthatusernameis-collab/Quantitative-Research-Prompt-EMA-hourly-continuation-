# EMA Hourly Continuation — PEPE/USDT P100_144

**Symbol:** PEPE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.5304 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8979 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -5.0639 |
| sortino_ratio | -1.6376 |
| max_drawdown | 0.8666 |
| cagr | -0.5486 |
| net_avg_win | 40.8523 |
| net_avg_loss | -65.2720 |
| avg_hold_time_bars | 3.5432 |
| exposure | 0.0839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
