# EMA Hourly Continuation — FLOW/USDT P21_89

**Symbol:** FLOW/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7596 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9705 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -1.9571 |
| sortino_ratio | -0.6031 |
| max_drawdown | 0.5349 |
| cagr | -0.2427 |
| net_avg_win | 69.6396 |
| net_avg_loss | -87.8298 |
| avg_hold_time_bars | 17.7253 |
| exposure | 0.3755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
