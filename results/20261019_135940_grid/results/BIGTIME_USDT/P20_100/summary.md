# EMA Hourly Continuation — BIGTIME/USDT P20_100

**Symbol:** BIGTIME/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.7302 |
| net_win_rate | 0.5058 |
| gross_profit_factor | 1.0448 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -2.4623 |
| sortino_ratio | -0.8559 |
| max_drawdown | 0.6720 |
| cagr | -0.3323 |
| net_avg_win | 56.5118 |
| net_avg_loss | -79.2046 |
| avg_hold_time_bars | 16.9372 |
| exposure | 0.4637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
