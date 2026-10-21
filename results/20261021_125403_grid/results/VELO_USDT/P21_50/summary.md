# EMA Hourly Continuation — VELO/USDT P21_50

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.6963 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.8616 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -2.2207 |
| sortino_ratio | -0.6901 |
| max_drawdown | 0.5765 |
| cagr | -0.2711 |
| net_avg_win | 55.5985 |
| net_avg_loss | -72.1841 |
| avg_hold_time_bars | 7.0210 |
| exposure | 0.1519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
