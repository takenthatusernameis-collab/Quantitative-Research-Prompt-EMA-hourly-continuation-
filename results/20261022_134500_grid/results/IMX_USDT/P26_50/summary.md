# EMA Hourly Continuation — IMX/USDT P26_50

**Symbol:** IMX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 946 |
| net_profit_factor | 0.5105 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.8850 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -5.9587 |
| sortino_ratio | -2.5756 |
| max_drawdown | 0.9588 |
| cagr | -0.7152 |
| net_avg_win | 22.0990 |
| net_avg_loss | -39.6115 |
| avg_hold_time_bars | 3.6163 |
| exposure | 0.1548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
