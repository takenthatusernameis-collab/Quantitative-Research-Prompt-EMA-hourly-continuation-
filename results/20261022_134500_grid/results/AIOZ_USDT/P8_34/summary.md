# EMA Hourly Continuation — AIOZ/USDT P8_34

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1474 |
| net_profit_factor | 0.6007 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.9257 |
| gross_win_rate | 0.4539 |
| sharpe_ratio | -8.6168 |
| sortino_ratio | -4.6072 |
| max_drawdown | 0.9970 |
| cagr | -0.8981 |
| net_avg_win | 23.0677 |
| net_avg_loss | -30.2934 |
| avg_hold_time_bars | 4.9708 |
| exposure | 0.3330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
