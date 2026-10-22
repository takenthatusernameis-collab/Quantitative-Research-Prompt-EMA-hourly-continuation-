# EMA Hourly Continuation — KCS/USDT P21_55

**Symbol:** KCS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.1973 |
| net_win_rate | 0.3264 |
| gross_profit_factor | 0.6550 |
| gross_win_rate | 0.3959 |
| sharpe_ratio | -13.9627 |
| sortino_ratio | -6.3606 |
| max_drawdown | 0.9998 |
| cagr | -0.9671 |
| net_avg_win | 7.8018 |
| net_avg_loss | -19.1626 |
| avg_hold_time_bars | 5.3845 |
| exposure | 0.2362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
