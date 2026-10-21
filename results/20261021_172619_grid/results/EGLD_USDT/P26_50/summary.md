# EMA Hourly Continuation — EGLD/USDT P26_50

**Symbol:** EGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.6492 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9309 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -2.7341 |
| sortino_ratio | -0.8394 |
| max_drawdown | 0.6634 |
| cagr | -0.3190 |
| net_avg_win | 51.3657 |
| net_avg_loss | -75.0835 |
| avg_hold_time_bars | 5.7598 |
| exposure | 0.1199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
