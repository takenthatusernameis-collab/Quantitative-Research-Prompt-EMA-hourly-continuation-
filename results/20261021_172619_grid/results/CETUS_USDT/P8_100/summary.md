# EMA Hourly Continuation — CETUS/USDT P8_100

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.9350 |
| net_win_rate | 0.5297 |
| gross_profit_factor | 1.1221 |
| gross_win_rate | 0.5297 |
| sharpe_ratio | -0.4224 |
| sortino_ratio | -0.1295 |
| max_drawdown | 0.2643 |
| cagr | -0.0641 |
| net_avg_win | 91.7924 |
| net_avg_loss | -110.5656 |
| avg_hold_time_bars | 33.2198 |
| exposure | 0.6840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
