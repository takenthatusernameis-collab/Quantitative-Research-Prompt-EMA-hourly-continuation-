# EMA Hourly Continuation — GLM/USDT P34_50

**Symbol:** GLM/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 869 |
| net_profit_factor | 0.3440 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.7959 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -8.0504 |
| sortino_ratio | -3.3764 |
| max_drawdown | 0.9852 |
| cagr | -0.8128 |
| net_avg_win | 13.0796 |
| net_avg_loss | -31.6830 |
| avg_hold_time_bars | 3.4960 |
| exposure | 0.1381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
