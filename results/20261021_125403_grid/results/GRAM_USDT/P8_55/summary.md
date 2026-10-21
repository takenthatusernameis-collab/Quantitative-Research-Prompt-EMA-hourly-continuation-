# EMA Hourly Continuation — GRAM/USDT P8_55

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.7553 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0258 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -2.2630 |
| sortino_ratio | -0.8085 |
| max_drawdown | 0.6542 |
| cagr | -0.3102 |
| net_avg_win | 59.8080 |
| net_avg_loss | -80.4699 |
| avg_hold_time_bars | 15.8647 |
| exposure | 0.4478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
