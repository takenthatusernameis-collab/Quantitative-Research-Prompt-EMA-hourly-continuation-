# EMA Hourly Continuation — SATS/USDT P34_100

**Symbol:** SATS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.6322 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.9191 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -3.5363 |
| sortino_ratio | -1.1818 |
| max_drawdown | 0.7798 |
| cagr | -0.4285 |
| net_avg_win | 49.2356 |
| net_avg_loss | -68.0792 |
| avg_hold_time_bars | 10.1272 |
| exposure | 0.2594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
