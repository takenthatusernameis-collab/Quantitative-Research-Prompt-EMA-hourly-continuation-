# EMA Hourly Continuation — CHR/USDT P20_21

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.7014 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 1.0018 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -1.7865 |
| sortino_ratio | -0.3916 |
| max_drawdown | 0.4084 |
| cagr | -0.1638 |
| net_avg_win | 73.5560 |
| net_avg_loss | -103.0942 |
| avg_hold_time_bars | 6.0085 |
| exposure | 0.0636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
