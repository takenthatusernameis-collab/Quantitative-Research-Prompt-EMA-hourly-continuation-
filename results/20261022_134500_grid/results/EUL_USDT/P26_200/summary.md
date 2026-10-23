# EMA Hourly Continuation — EUL/USDT P26_200

**Symbol:** EUL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.5573 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.7516 |
| gross_win_rate | 0.4447 |
| sharpe_ratio | -3.4156 |
| sortino_ratio | -1.0103 |
| max_drawdown | 0.7088 |
| cagr | -0.3794 |
| net_avg_win | 44.8489 |
| net_avg_loss | -63.8577 |
| avg_hold_time_bars | 23.8713 |
| exposure | 0.4807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
