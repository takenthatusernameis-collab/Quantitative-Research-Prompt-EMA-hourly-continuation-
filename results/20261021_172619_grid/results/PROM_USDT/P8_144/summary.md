# EMA Hourly Continuation — PROM/USDT P8_144

**Symbol:** PROM/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.5868 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.7569 |
| gross_win_rate | 0.4327 |
| sharpe_ratio | -3.6053 |
| sortino_ratio | -1.1167 |
| max_drawdown | 0.7344 |
| cagr | -0.4049 |
| net_avg_win | 49.4893 |
| net_avg_loss | -64.3331 |
| avg_hold_time_bars | 30.1470 |
| exposure | 0.6619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
