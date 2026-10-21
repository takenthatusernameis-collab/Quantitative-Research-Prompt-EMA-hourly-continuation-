# EMA Hourly Continuation — LQTY/USDT P8_26

**Symbol:** LQTY/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.6853 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9237 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -3.3528 |
| sortino_ratio | -1.3606 |
| max_drawdown | 0.8032 |
| cagr | -0.4633 |
| net_avg_win | 43.9873 |
| net_avg_loss | -60.3408 |
| avg_hold_time_bars | 6.8850 |
| exposure | 0.2520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
