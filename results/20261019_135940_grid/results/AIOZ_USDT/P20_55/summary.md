# EMA Hourly Continuation — AIOZ/USDT P20_55

**Symbol:** AIOZ/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1039 |
| net_profit_factor | 0.6222 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.9463 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -6.7165 |
| sortino_ratio | -3.0379 |
| max_drawdown | 0.9775 |
| cagr | -0.7727 |
| net_avg_win | 33.9041 |
| net_avg_loss | -45.7139 |
| avg_hold_time_bars | 5.2676 |
| exposure | 0.2488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
