# EMA Hourly Continuation — ARPA/USDT P12_100

**Symbol:** ARPA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 810 |
| net_profit_factor | 0.5553 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.8602 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -5.8298 |
| sortino_ratio | -2.3222 |
| max_drawdown | 0.9432 |
| cagr | -0.6747 |
| net_avg_win | 32.8249 |
| net_avg_loss | -46.8207 |
| avg_hold_time_bars | 14.6012 |
| exposure | 0.5352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
