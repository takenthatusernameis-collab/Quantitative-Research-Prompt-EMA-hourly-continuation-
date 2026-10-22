# EMA Hourly Continuation — BLUR/USDT P21_144

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.8932 |
| net_win_rate | 0.5207 |
| gross_profit_factor | 1.0907 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -0.6562 |
| sortino_ratio | -0.1792 |
| max_drawdown | 0.2774 |
| cagr | -0.0827 |
| net_avg_win | 86.5998 |
| net_avg_loss | -105.3145 |
| avg_hold_time_bars | 36.5647 |
| exposure | 0.6006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
