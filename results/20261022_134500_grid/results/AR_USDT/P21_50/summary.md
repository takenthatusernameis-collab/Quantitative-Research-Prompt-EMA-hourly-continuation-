# EMA Hourly Continuation — AR/USDT P21_50

**Symbol:** AR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1009 |
| net_profit_factor | 0.4397 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.7161 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -7.3898 |
| sortino_ratio | -3.2978 |
| max_drawdown | 0.9827 |
| cagr | -0.8011 |
| net_avg_win | 17.6095 |
| net_avg_loss | -30.7178 |
| avg_hold_time_bars | 4.3548 |
| exposure | 0.1997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
