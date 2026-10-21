# EMA Hourly Continuation — ZETA/USDT P34_55

**Symbol:** ZETA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.6247 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8804 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -3.1920 |
| sortino_ratio | -0.9050 |
| max_drawdown | 0.6580 |
| cagr | -0.3390 |
| net_avg_win | 59.2672 |
| net_avg_loss | -81.0701 |
| avg_hold_time_bars | 5.5241 |
| exposure | 0.0987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
