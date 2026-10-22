# EMA Hourly Continuation — FLIP/USDT P50_100

**Symbol:** FLIP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.5307 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.7952 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -3.3870 |
| sortino_ratio | -0.8243 |
| max_drawdown | 0.6380 |
| cagr | -0.3205 |
| net_avg_win | 54.4443 |
| net_avg_loss | -79.7182 |
| avg_hold_time_bars | 14.0814 |
| exposure | 0.1888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
