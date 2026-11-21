# EMA Hourly Continuation — HTR/USDT P12_100

**Symbol:** HTR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 850 |
| net_profit_factor | 0.4850 |
| net_win_rate | 0.3859 |
| gross_profit_factor | 0.6966 |
| gross_win_rate | 0.3953 |
| sharpe_ratio | -7.4945 |
| sortino_ratio | -3.0427 |
| max_drawdown | 0.9770 |
| cagr | -0.7768 |
| net_avg_win | 28.0431 |
| net_avg_loss | -36.3348 |
| avg_hold_time_bars | 12.4106 |
| exposure | 0.4795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
