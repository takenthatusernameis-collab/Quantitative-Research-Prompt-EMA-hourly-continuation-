# EMA Hourly Continuation — MOCA/USDT P26_55

**Symbol:** MOCA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.6310 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.8626 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -3.2995 |
| sortino_ratio | -1.0320 |
| max_drawdown | 0.6915 |
| cagr | -0.3759 |
| net_avg_win | 56.0038 |
| net_avg_loss | -75.9107 |
| avg_hold_time_bars | 6.5757 |
| exposure | 0.1437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
