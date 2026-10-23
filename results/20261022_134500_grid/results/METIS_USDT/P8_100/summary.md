# EMA Hourly Continuation — METIS/USDT P8_100

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.6793 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9492 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -3.6296 |
| sortino_ratio | -1.2590 |
| max_drawdown | 0.7960 |
| cagr | -0.4569 |
| net_avg_win | 57.2739 |
| net_avg_loss | -75.0030 |
| avg_hold_time_bars | 24.1591 |
| exposure | 0.6765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
