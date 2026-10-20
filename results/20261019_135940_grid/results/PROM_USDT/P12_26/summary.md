# EMA Hourly Continuation — PROM/USDT P12_26

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1337 |
| net_profit_factor | 0.4749 |
| net_win_rate | 0.4099 |
| gross_profit_factor | 1.0178 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -11.3357 |
| sortino_ratio | -5.8601 |
| max_drawdown | 0.9994 |
| cagr | -0.9487 |
| net_avg_win | 16.4966 |
| net_avg_loss | -24.1247 |
| avg_hold_time_bars | 4.0688 |
| exposure | 0.2473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
