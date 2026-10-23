# EMA Hourly Continuation — POPCAT/USDT P12_50

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 925 |
| net_profit_factor | 0.6215 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8652 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -5.8316 |
| sortino_ratio | -2.6906 |
| max_drawdown | 0.9376 |
| cagr | -0.7229 |
| net_avg_win | 36.9178 |
| net_avg_loss | -48.7605 |
| avg_hold_time_bars | 7.0605 |
| exposure | 0.3450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
