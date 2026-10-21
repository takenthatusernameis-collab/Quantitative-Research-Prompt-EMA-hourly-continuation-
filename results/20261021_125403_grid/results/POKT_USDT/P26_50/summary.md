# EMA Hourly Continuation — POKT/USDT P26_50

**Symbol:** POKT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.6000 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.8062 |
| gross_win_rate | 0.4289 |
| sharpe_ratio | -3.7569 |
| sortino_ratio | -1.1005 |
| max_drawdown | 0.7373 |
| cagr | -0.3990 |
| net_avg_win | 58.9578 |
| net_avg_loss | -73.7941 |
| avg_hold_time_bars | 7.8671 |
| exposure | 0.1527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
