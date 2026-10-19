# EMA Hourly Continuation — AAVE/USDT P12_100

**Symbol:** AAVE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.5549 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8410 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -4.3010 |
| sortino_ratio | -1.5033 |
| max_drawdown | 0.8464 |
| cagr | -0.5117 |
| net_avg_win | 36.9078 |
| net_avg_loss | -55.9854 |
| avg_hold_time_bars | 20.6370 |
| exposure | 0.5788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
