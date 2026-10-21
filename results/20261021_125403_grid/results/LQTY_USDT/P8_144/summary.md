# EMA Hourly Continuation — LQTY/USDT P8_144

**Symbol:** LQTY/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7299 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.8652 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -1.6972 |
| sortino_ratio | -0.4381 |
| max_drawdown | 0.4190 |
| cagr | -0.1834 |
| net_avg_win | 69.3123 |
| net_avg_loss | -84.1756 |
| avg_hold_time_bars | 51.4880 |
| exposure | 0.7735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
