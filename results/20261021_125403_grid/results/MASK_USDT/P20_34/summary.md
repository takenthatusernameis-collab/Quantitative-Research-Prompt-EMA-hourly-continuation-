# EMA Hourly Continuation — MASK/USDT P20_34

**Symbol:** MASK/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.5802 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9160 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -3.7463 |
| sortino_ratio | -1.1516 |
| max_drawdown | 0.7411 |
| cagr | -0.4142 |
| net_avg_win | 46.6395 |
| net_avg_loss | -72.4434 |
| avg_hold_time_bars | 6.0000 |
| exposure | 0.1260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
