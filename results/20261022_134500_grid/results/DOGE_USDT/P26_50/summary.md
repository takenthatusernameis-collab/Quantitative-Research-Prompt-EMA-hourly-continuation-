# EMA Hourly Continuation — DOGE/USDT P26_50

**Symbol:** DOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 942 |
| net_profit_factor | 0.3437 |
| net_win_rate | 0.4087 |
| gross_profit_factor | 0.7695 |
| gross_win_rate | 0.4406 |
| sharpe_ratio | -9.8060 |
| sortino_ratio | -4.2725 |
| max_drawdown | 0.9958 |
| cagr | -0.8850 |
| net_avg_win | 13.5452 |
| net_avg_loss | -27.2372 |
| avg_hold_time_bars | 3.7059 |
| exposure | 0.1587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
