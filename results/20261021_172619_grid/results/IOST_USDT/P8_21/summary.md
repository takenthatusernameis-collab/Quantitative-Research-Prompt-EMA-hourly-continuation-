# EMA Hourly Continuation — IOST/USDT P8_21

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 774 |
| net_profit_factor | 0.6734 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0501 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -3.8157 |
| sortino_ratio | -1.5277 |
| max_drawdown | 0.8304 |
| cagr | -0.5030 |
| net_avg_win | 43.8362 |
| net_avg_loss | -65.7773 |
| avg_hold_time_bars | 5.5930 |
| exposure | 0.1968 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
