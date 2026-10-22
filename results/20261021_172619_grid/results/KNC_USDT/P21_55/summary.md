# EMA Hourly Continuation — KNC/USDT P21_55

**Symbol:** KNC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6731 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9912 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -3.8368 |
| sortino_ratio | -1.3551 |
| max_drawdown | 0.8011 |
| cagr | -0.4634 |
| net_avg_win | 56.1242 |
| net_avg_loss | -75.8041 |
| avg_hold_time_bars | 9.3202 |
| exposure | 0.2580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
