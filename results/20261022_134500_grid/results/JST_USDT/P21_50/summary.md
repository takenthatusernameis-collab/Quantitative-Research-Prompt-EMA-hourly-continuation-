# EMA Hourly Continuation — JST/USDT P21_50

**Symbol:** JST/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 849 |
| net_profit_factor | 0.2551 |
| net_win_rate | 0.4052 |
| gross_profit_factor | 0.9996 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -9.8224 |
| sortino_ratio | -4.1032 |
| max_drawdown | 0.9951 |
| cagr | -0.8773 |
| net_avg_win | 9.9074 |
| net_avg_loss | -26.4511 |
| avg_hold_time_bars | 5.2344 |
| exposure | 0.2011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
