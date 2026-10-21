# EMA Hourly Continuation — VELO/USDT P20_34

**Symbol:** VELO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7029 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.9092 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -1.8948 |
| sortino_ratio | -0.4664 |
| max_drawdown | 0.4336 |
| cagr | -0.1926 |
| net_avg_win | 69.2666 |
| net_avg_loss | -90.2784 |
| avg_hold_time_bars | 5.2222 |
| exposure | 0.0705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
