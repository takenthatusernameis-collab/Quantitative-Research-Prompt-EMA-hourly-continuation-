# EMA Hourly Continuation — LINK/USDT P8_55

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.7860 |
| net_win_rate | 0.4960 |
| gross_profit_factor | 0.9982 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -2.0877 |
| sortino_ratio | -0.7447 |
| max_drawdown | 0.6035 |
| cagr | -0.2904 |
| net_avg_win | 68.8785 |
| net_avg_loss | -86.2286 |
| avg_hold_time_bars | 15.8052 |
| exposure | 0.4461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
