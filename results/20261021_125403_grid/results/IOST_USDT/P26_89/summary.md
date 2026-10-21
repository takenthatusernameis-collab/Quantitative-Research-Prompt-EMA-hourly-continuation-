# EMA Hourly Continuation — IOST/USDT P26_89

**Symbol:** IOST/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.8435 |
| net_win_rate | 0.5360 |
| gross_profit_factor | 1.1439 |
| gross_win_rate | 0.5360 |
| sharpe_ratio | -1.1108 |
| sortino_ratio | -0.3485 |
| max_drawdown | 0.3629 |
| cagr | -0.1499 |
| net_avg_win | 71.3539 |
| net_avg_loss | -97.7246 |
| avg_hold_time_bars | 15.2076 |
| exposure | 0.3263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
