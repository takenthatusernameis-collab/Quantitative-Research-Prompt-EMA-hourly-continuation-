# EMA Hourly Continuation — IOTX/USDT P26_50

**Symbol:** IOTX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.5258 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 1.0198 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -8.1558 |
| sortino_ratio | -3.6031 |
| max_drawdown | 0.9890 |
| cagr | -0.8312 |
| net_avg_win | 25.3729 |
| net_avg_loss | -38.3910 |
| avg_hold_time_bars | 3.7251 |
| exposure | 0.1651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
