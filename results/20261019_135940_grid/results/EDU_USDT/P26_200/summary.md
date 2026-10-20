# EMA Hourly Continuation — EDU/USDT P26_200

**Symbol:** EDU/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.6418 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.8379 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -2.9102 |
| sortino_ratio | -0.8428 |
| max_drawdown | 0.6580 |
| cagr | -0.3348 |
| net_avg_win | 58.7335 |
| net_avg_loss | -75.6767 |
| avg_hold_time_bars | 29.4573 |
| exposure | 0.5772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
