# EMA Hourly Continuation — CARV/USDT P50_55

**Symbol:** CARV/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.2600 |
| net_win_rate | 0.3849 |
| gross_profit_factor | 0.8203 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -9.6222 |
| sortino_ratio | -3.5202 |
| max_drawdown | 0.9777 |
| cagr | -0.8458 |
| net_avg_win | 17.2607 |
| net_avg_loss | -41.5395 |
| avg_hold_time_bars | 2.4197 |
| exposure | 0.0704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
