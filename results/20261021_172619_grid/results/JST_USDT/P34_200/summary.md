# EMA Hourly Continuation — JST/USDT P34_200

**Symbol:** JST/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7405 |
| net_win_rate | 0.5281 |
| gross_profit_factor | 1.0916 |
| gross_win_rate | 0.5281 |
| sharpe_ratio | -1.4574 |
| sortino_ratio | -0.3599 |
| max_drawdown | 0.3817 |
| cagr | -0.1569 |
| net_avg_win | 62.3887 |
| net_avg_loss | -94.2665 |
| avg_hold_time_bars | 33.9307 |
| exposure | 0.4652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
