# EMA Hourly Continuation — BOME/USDT P21_55

**Symbol:** BOME/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.4915 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.7771 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -5.6690 |
| sortino_ratio | -2.3856 |
| max_drawdown | 0.9513 |
| cagr | -0.6865 |
| net_avg_win | 22.1366 |
| net_avg_loss | -38.1132 |
| avg_hold_time_bars | 5.4972 |
| exposure | 0.2251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
