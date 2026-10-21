# EMA Hourly Continuation — DGB/USDT P8_21

**Symbol:** DGB/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.7955 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.1133 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -1.9769 |
| sortino_ratio | -0.6462 |
| max_drawdown | 0.5810 |
| cagr | -0.2565 |
| net_avg_win | 77.0635 |
| net_avg_loss | -102.2730 |
| avg_hold_time_bars | 5.5097 |
| exposure | 0.1292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
