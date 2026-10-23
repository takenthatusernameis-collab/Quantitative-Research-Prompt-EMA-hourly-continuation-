# EMA Hourly Continuation — GALA/USDT P21_55

**Symbol:** GALA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.4751 |
| net_win_rate | 0.4320 |
| gross_profit_factor | 0.8019 |
| gross_win_rate | 0.4380 |
| sharpe_ratio | -7.5249 |
| sortino_ratio | -3.3720 |
| max_drawdown | 0.9841 |
| cagr | -0.8013 |
| net_avg_win | 20.5887 |
| net_avg_loss | -32.9605 |
| avg_hold_time_bars | 4.8620 |
| exposure | 0.2210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
