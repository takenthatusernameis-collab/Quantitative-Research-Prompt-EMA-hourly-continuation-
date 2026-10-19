# EMA Hourly Continuation — COMP/USDT P21_144

**Symbol:** COMP/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.6431 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 1.0150 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -3.1357 |
| sortino_ratio | -1.0209 |
| max_drawdown | 0.7235 |
| cagr | -0.3888 |
| net_avg_win | 47.8869 |
| net_avg_loss | -73.3654 |
| avg_hold_time_bars | 21.9888 |
| exposure | 0.5377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
