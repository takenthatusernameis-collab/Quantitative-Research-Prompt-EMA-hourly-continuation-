# EMA Hourly Continuation — MOG/USDT P34_50

**Symbol:** MOG/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 823 |
| net_profit_factor | 0.5575 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.8783 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -7.0832 |
| sortino_ratio | -3.0006 |
| max_drawdown | 0.9662 |
| cagr | -0.7704 |
| net_avg_win | 33.4334 |
| net_avg_loss | -47.5573 |
| avg_hold_time_bars | 2.5808 |
| exposure | 0.1056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
