# EMA Hourly Continuation — POLYX/USDT P20_26

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6705 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0802 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -2.4548 |
| sortino_ratio | -0.6489 |
| max_drawdown | 0.5613 |
| cagr | -0.2574 |
| net_avg_win | 62.2606 |
| net_avg_loss | -97.3921 |
| avg_hold_time_bars | 4.5893 |
| exposure | 0.0701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
