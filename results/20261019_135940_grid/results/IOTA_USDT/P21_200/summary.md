# EMA Hourly Continuation — IOTA/USDT P21_200

**Symbol:** IOTA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7583 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0437 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -1.5732 |
| sortino_ratio | -0.4056 |
| max_drawdown | 0.4189 |
| cagr | -0.1762 |
| net_avg_win | 71.5294 |
| net_avg_loss | -96.0367 |
| avg_hold_time_bars | 41.8687 |
| exposure | 0.6375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
