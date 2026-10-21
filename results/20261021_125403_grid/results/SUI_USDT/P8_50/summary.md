# EMA Hourly Continuation — SUI/USDT P8_50

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.8754 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0884 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -1.0588 |
| sortino_ratio | -0.3820 |
| max_drawdown | 0.4048 |
| cagr | -0.1652 |
| net_avg_win | 78.1070 |
| net_avg_loss | -97.5523 |
| avg_hold_time_bars | 13.9904 |
| exposure | 0.3994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
