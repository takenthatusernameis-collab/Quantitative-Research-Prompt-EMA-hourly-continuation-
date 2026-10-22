# EMA Hourly Continuation — CTSI/USDT P50_100

**Symbol:** CTSI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.6883 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9390 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -2.6076 |
| sortino_ratio | -0.8062 |
| max_drawdown | 0.6142 |
| cagr | -0.3087 |
| net_avg_win | 59.0375 |
| net_avg_loss | -80.4398 |
| avg_hold_time_bars | 8.5824 |
| exposure | 0.1822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
