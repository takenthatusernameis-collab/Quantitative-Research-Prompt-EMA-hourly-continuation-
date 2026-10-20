# EMA Hourly Continuation — LQTY/USDT P8_50

**Symbol:** LQTY/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.5126 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.7833 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -5.7086 |
| sortino_ratio | -2.5308 |
| max_drawdown | 0.9558 |
| cagr | -0.7057 |
| net_avg_win | 21.8694 |
| net_avg_loss | -35.9945 |
| avg_hold_time_bars | 11.3509 |
| exposure | 0.5152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
