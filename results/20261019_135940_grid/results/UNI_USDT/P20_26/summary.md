# EMA Hourly Continuation — UNI/USDT P20_26

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.2122 |
| net_win_rate | 0.3564 |
| gross_profit_factor | 0.6722 |
| gross_win_rate | 0.3942 |
| sharpe_ratio | -14.7111 |
| sortino_ratio | -7.4779 |
| max_drawdown | 1.0000 |
| cagr | -0.9813 |
| net_avg_win | 6.2215 |
| net_avg_loss | -16.2320 |
| avg_hold_time_bars | 1.7630 |
| exposure | 0.0974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
