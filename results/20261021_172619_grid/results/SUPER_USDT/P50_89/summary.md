# EMA Hourly Continuation — SUPER/USDT P50_89

**Symbol:** SUPER/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.8035 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.0885 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -1.2198 |
| sortino_ratio | -0.3342 |
| max_drawdown | 0.3501 |
| cagr | -0.1425 |
| net_avg_win | 68.9474 |
| net_avg_loss | -95.3411 |
| avg_hold_time_bars | 8.3767 |
| exposure | 0.1375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
