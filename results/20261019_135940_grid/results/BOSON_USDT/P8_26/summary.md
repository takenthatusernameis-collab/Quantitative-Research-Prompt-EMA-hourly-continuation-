# EMA Hourly Continuation — BOSON/USDT P8_26

**Symbol:** BOSON/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1299 |
| net_profit_factor | 0.5042 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.8617 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -8.2772 |
| sortino_ratio | -4.1705 |
| max_drawdown | 0.9942 |
| cagr | -0.8695 |
| net_avg_win | 18.0188 |
| net_avg_loss | -27.1660 |
| avg_hold_time_bars | 4.9777 |
| exposure | 0.2939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
