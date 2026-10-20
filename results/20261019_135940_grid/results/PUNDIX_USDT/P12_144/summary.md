# EMA Hourly Continuation — PUNDIX/USDT P12_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.6366 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9537 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -2.9886 |
| sortino_ratio | -0.9197 |
| max_drawdown | 0.6824 |
| cagr | -0.3578 |
| net_avg_win | 50.4525 |
| net_avg_loss | -75.3732 |
| avg_hold_time_bars | 31.8222 |
| exposure | 0.6914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
