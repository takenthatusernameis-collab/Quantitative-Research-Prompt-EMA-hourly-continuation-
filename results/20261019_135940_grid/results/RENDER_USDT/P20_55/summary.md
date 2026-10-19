# EMA Hourly Continuation — RENDER/USDT P20_55

**Symbol:** RENDER/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 857 |
| net_profit_factor | 0.5589 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.9267 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -6.2763 |
| sortino_ratio | -2.7757 |
| max_drawdown | 0.9498 |
| cagr | -0.7440 |
| net_avg_win | 29.7932 |
| net_avg_loss | -47.3163 |
| avg_hold_time_bars | 4.7258 |
| exposure | 0.2138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
