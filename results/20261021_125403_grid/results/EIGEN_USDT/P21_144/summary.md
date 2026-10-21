# EMA Hourly Continuation — EIGEN/USDT P21_144

**Symbol:** EIGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.8599 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 0.9928 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -0.8780 |
| sortino_ratio | -0.2372 |
| max_drawdown | 0.2251 |
| cagr | -0.1060 |
| net_avg_win | 86.8809 |
| net_avg_loss | -100.3457 |
| avg_hold_time_bars | 31.9244 |
| exposure | 0.5169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
