# EMA Hourly Continuation — AGLD/USDT P26_55

**Symbol:** AGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 920 |
| net_profit_factor | 0.5202 |
| net_win_rate | 0.4413 |
| gross_profit_factor | 0.9019 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -6.6869 |
| sortino_ratio | -2.8594 |
| max_drawdown | 0.9693 |
| cagr | -0.7461 |
| net_avg_win | 25.8606 |
| net_avg_loss | -39.2692 |
| avg_hold_time_bars | 5.1924 |
| exposure | 0.2162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
