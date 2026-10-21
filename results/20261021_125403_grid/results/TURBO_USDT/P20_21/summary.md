# EMA Hourly Continuation — TURBO/USDT P20_21

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 114 |
| net_profit_factor | 0.9841 |
| net_win_rate | 0.5789 |
| gross_profit_factor | 1.3616 |
| gross_win_rate | 0.5789 |
| sharpe_ratio | -0.0234 |
| sortino_ratio | -0.0040 |
| max_drawdown | 0.1261 |
| cagr | -0.0044 |
| net_avg_win | 86.0347 |
| net_avg_loss | -120.2035 |
| avg_hold_time_bars | 4.2281 |
| exposure | 0.0263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
