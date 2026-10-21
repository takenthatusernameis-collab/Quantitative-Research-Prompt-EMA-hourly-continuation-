# EMA Hourly Continuation — UMA/USDT P20_89

**Symbol:** UMA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.7463 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9728 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -2.1370 |
| sortino_ratio | -0.7077 |
| max_drawdown | 0.5851 |
| cagr | -0.2782 |
| net_avg_win | 61.8290 |
| net_avg_loss | -81.3168 |
| avg_hold_time_bars | 15.4283 |
| exposure | 0.3766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
