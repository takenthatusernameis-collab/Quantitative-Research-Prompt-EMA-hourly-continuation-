# EMA Hourly Continuation — HTR/USDT P20_50

**Symbol:** HTR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.4393 |
| net_win_rate | 0.3767 |
| gross_profit_factor | 0.7151 |
| gross_win_rate | 0.3882 |
| sharpe_ratio | -9.1826 |
| sortino_ratio | -3.9928 |
| max_drawdown | 0.9934 |
| cagr | -0.8610 |
| net_avg_win | 21.6697 |
| net_avg_loss | -29.8131 |
| avg_hold_time_bars | 5.4827 |
| exposure | 0.2375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
