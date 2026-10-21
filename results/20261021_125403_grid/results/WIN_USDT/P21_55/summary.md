# EMA Hourly Continuation — WIN/USDT P21_55

**Symbol:** WIN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.5482 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.8230 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -3.9370 |
| sortino_ratio | -1.2100 |
| max_drawdown | 0.7759 |
| cagr | -0.4266 |
| net_avg_win | 43.9050 |
| net_avg_loss | -65.8412 |
| avg_hold_time_bars | 8.5835 |
| exposure | 0.1799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
