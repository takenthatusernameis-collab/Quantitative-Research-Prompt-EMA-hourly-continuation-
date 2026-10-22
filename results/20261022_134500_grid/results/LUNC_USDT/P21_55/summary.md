# EMA Hourly Continuation — LUNC/USDT P21_55

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1023 |
| net_profit_factor | 0.3584 |
| net_win_rate | 0.4223 |
| gross_profit_factor | 0.7233 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -9.0832 |
| sortino_ratio | -4.1122 |
| max_drawdown | 0.9940 |
| cagr | -0.8681 |
| net_avg_win | 12.8489 |
| net_avg_loss | -26.2081 |
| avg_hold_time_bars | 4.5973 |
| exposure | 0.2138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
