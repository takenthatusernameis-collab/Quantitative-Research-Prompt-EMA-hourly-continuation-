# EMA Hourly Continuation — CPOOL/USDT P50_89

**Symbol:** CPOOL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.7389 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9081 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -1.7902 |
| sortino_ratio | -0.4619 |
| max_drawdown | 0.4685 |
| cagr | -0.1918 |
| net_avg_win | 75.1240 |
| net_avg_loss | -92.2161 |
| avg_hold_time_bars | 5.8018 |
| exposure | 0.0865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
