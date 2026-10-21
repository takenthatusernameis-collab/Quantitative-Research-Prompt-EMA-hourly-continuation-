# EMA Hourly Continuation — KCS/USDT P21_50

**Symbol:** KCS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.3803 |
| net_win_rate | 0.3973 |
| gross_profit_factor | 0.7355 |
| gross_win_rate | 0.4041 |
| sharpe_ratio | -6.5156 |
| sortino_ratio | -1.9887 |
| max_drawdown | 0.9067 |
| cagr | -0.6072 |
| net_avg_win | 31.5263 |
| net_avg_loss | -54.6511 |
| avg_hold_time_bars | 8.1558 |
| exposure | 0.1642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
