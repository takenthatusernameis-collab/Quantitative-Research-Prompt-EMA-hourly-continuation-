# EMA Hourly Continuation — IOST/USDT P50_89

**Symbol:** IOST/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.7114 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0629 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -2.3150 |
| sortino_ratio | -0.6694 |
| max_drawdown | 0.5489 |
| cagr | -0.2648 |
| net_avg_win | 64.3991 |
| net_avg_loss | -94.1792 |
| avg_hold_time_bars | 7.5668 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
