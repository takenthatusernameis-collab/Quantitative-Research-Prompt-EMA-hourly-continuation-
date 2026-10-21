# EMA Hourly Continuation — ANKR/USDT P8_50

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.7220 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9546 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -3.2073 |
| sortino_ratio | -1.1784 |
| max_drawdown | 0.7536 |
| cagr | -0.4189 |
| net_avg_win | 61.3588 |
| net_avg_loss | -76.9255 |
| avg_hold_time_bars | 17.0136 |
| exposure | 0.5127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
