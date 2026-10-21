# EMA Hourly Continuation — SQD/USDT P34_50

**Symbol:** SQD/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.7908 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0225 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.2958 |
| sortino_ratio | -0.3163 |
| max_drawdown | 0.3442 |
| cagr | -0.1350 |
| net_avg_win | 79.5998 |
| net_avg_loss | -102.1012 |
| avg_hold_time_bars | 6.1679 |
| exposure | 0.0812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
