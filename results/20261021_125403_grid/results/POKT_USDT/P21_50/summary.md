# EMA Hourly Continuation — POKT/USDT P21_50

**Symbol:** POKT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.6423 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.8510 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -3.7899 |
| sortino_ratio | -1.2388 |
| max_drawdown | 0.7766 |
| cagr | -0.4355 |
| net_avg_win | 58.6115 |
| net_avg_loss | -71.1730 |
| avg_hold_time_bars | 7.8390 |
| exposure | 0.1894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
