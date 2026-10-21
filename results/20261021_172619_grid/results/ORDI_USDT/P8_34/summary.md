# EMA Hourly Continuation — ORDI/USDT P8_34

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.7306 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9105 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -2.9118 |
| sortino_ratio | -1.1091 |
| max_drawdown | 0.7296 |
| cagr | -0.3997 |
| net_avg_win | 58.1459 |
| net_avg_loss | -70.9500 |
| avg_hold_time_bars | 9.6154 |
| exposure | 0.3125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
