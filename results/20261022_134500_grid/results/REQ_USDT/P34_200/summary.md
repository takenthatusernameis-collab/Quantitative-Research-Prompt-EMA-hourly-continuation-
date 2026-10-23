# EMA Hourly Continuation — REQ/USDT P34_200

**Symbol:** REQ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.4670 |
| net_win_rate | 0.3993 |
| gross_profit_factor | 0.8334 |
| gross_win_rate | 0.4219 |
| sharpe_ratio | -6.6473 |
| sortino_ratio | -2.2436 |
| max_drawdown | 0.9397 |
| cagr | -0.6731 |
| net_avg_win | 35.8011 |
| net_avg_loss | -50.9567 |
| avg_hold_time_bars | 16.9306 |
| exposure | 0.4433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
