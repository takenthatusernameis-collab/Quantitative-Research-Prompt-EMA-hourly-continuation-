# EMA Hourly Continuation — BRETT/USDT P20_26

**Symbol:** BRETT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1126 |
| net_profit_factor | 0.3222 |
| net_win_rate | 0.3979 |
| gross_profit_factor | 0.6748 |
| gross_win_rate | 0.4245 |
| sharpe_ratio | -11.4582 |
| sortino_ratio | -5.6208 |
| max_drawdown | 0.9990 |
| cagr | -0.9444 |
| net_avg_win | 10.5993 |
| net_avg_loss | -21.7374 |
| avg_hold_time_bars | 2.0222 |
| exposure | 0.1096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
