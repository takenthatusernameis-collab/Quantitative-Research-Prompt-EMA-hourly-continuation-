# EMA Hourly Continuation — MASK/USDT P12_50

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.6046 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8509 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -4.2970 |
| sortino_ratio | -1.6492 |
| max_drawdown | 0.8516 |
| cagr | -0.5322 |
| net_avg_win | 39.0993 |
| net_avg_loss | -54.8002 |
| avg_hold_time_bars | 10.4077 |
| exposure | 0.3435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
