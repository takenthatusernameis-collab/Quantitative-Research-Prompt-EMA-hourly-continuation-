# EMA Hourly Continuation — ENA/USDT P21_144

**Symbol:** ENA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.8579 |
| net_win_rate | 0.4960 |
| gross_profit_factor | 0.9765 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -0.8628 |
| sortino_ratio | -0.2380 |
| max_drawdown | 0.2784 |
| cagr | -0.1065 |
| net_avg_win | 80.3621 |
| net_avg_loss | -92.1793 |
| avg_hold_time_bars | 28.9973 |
| exposure | 0.4916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
