# EMA Hourly Continuation — MOVR/USDT P34_50

**Symbol:** MOVR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.7973 |
| net_win_rate | 0.5316 |
| gross_profit_factor | 1.1339 |
| gross_win_rate | 0.5316 |
| sharpe_ratio | -1.2210 |
| sortino_ratio | -0.3062 |
| max_drawdown | 0.3997 |
| cagr | -0.1309 |
| net_avg_win | 72.9622 |
| net_avg_loss | -103.8472 |
| avg_hold_time_bars | 5.1694 |
| exposure | 0.0707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
