# EMA Hourly Continuation — AR/USDT P26_55

**Symbol:** AR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.7701 |
| net_win_rate | 0.5078 |
| gross_profit_factor | 0.9914 |
| gross_win_rate | 0.5078 |
| sharpe_ratio | -1.5163 |
| sortino_ratio | -0.4613 |
| max_drawdown | 0.4471 |
| cagr | -0.1917 |
| net_avg_win | 60.8312 |
| net_avg_loss | -81.4915 |
| avg_hold_time_bars | 7.3051 |
| exposure | 0.1491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
