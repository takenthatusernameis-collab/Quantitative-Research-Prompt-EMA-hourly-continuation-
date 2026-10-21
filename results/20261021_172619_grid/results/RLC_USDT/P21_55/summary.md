# EMA Hourly Continuation — RLC/USDT P21_55

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.6959 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9627 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -2.7589 |
| sortino_ratio | -0.9313 |
| max_drawdown | 0.6678 |
| cagr | -0.3473 |
| net_avg_win | 54.9226 |
| net_avg_loss | -76.6815 |
| avg_hold_time_bars | 7.5917 |
| exposure | 0.1919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
