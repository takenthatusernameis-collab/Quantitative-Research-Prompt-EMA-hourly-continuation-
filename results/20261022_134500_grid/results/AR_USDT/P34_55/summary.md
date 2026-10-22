# EMA Hourly Continuation — AR/USDT P34_55

**Symbol:** AR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.3607 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.6511 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -7.2049 |
| sortino_ratio | -3.0584 |
| max_drawdown | 0.9760 |
| cagr | -0.7737 |
| net_avg_win | 13.8348 |
| net_avg_loss | -30.4724 |
| avg_hold_time_bars | 3.3215 |
| exposure | 0.1357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
