# EMA Hourly Continuation — TURBO/USDT P55_100

**Symbol:** TURBO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.6443 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 1.0124 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -4.2059 |
| sortino_ratio | -1.5303 |
| max_drawdown | 0.8022 |
| cagr | -0.5211 |
| net_avg_win | 53.5060 |
| net_avg_loss | -76.4373 |
| avg_hold_time_bars | 4.8973 |
| exposure | 0.1483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
