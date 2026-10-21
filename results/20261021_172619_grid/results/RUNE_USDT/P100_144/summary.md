# EMA Hourly Continuation — RUNE/USDT P100_144

**Symbol:** RUNE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.6598 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -1.7632 |
| sortino_ratio | -0.3705 |
| max_drawdown | 0.3583 |
| cagr | -0.1554 |
| net_avg_win | 64.4757 |
| net_avg_loss | -91.5544 |
| avg_hold_time_bars | 6.5349 |
| exposure | 0.0639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
