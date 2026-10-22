# EMA Hourly Continuation — UQC/USDT P34_50

**Symbol:** UQC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.3091 |
| net_win_rate | 0.2727 |
| gross_profit_factor | 0.4475 |
| gross_win_rate | 0.2775 |
| sharpe_ratio | -5.5268 |
| sortino_ratio | -1.1239 |
| max_drawdown | 0.7490 |
| cagr | -0.4216 |
| net_avg_win | 58.7536 |
| net_avg_loss | -71.2845 |
| avg_hold_time_bars | 46.2727 |
| exposure | 0.4377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
