# EMA Hourly Continuation — AAVE/USDT P26_50

**Symbol:** AAVE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7211 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9749 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -2.0578 |
| sortino_ratio | -0.5593 |
| max_drawdown | 0.4936 |
| cagr | -0.2259 |
| net_avg_win | 69.6623 |
| net_avg_loss | -92.4102 |
| avg_hold_time_bars | 6.4917 |
| exposure | 0.1062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
