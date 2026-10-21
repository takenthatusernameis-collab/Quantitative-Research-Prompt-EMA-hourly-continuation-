# EMA Hourly Continuation — POPCAT/USDT P8_34

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.7841 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9609 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -2.2306 |
| sortino_ratio | -0.8794 |
| max_drawdown | 0.5943 |
| cagr | -0.3342 |
| net_avg_win | 65.9596 |
| net_avg_loss | -81.3422 |
| avg_hold_time_bars | 8.8824 |
| exposure | 0.3073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
