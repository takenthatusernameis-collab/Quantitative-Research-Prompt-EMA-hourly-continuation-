# EMA Hourly Continuation — ZETA/USDT P20_144

**Symbol:** ZETA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.8807 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0405 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -0.7254 |
| sortino_ratio | -0.1830 |
| max_drawdown | 0.3630 |
| cagr | -0.0833 |
| net_avg_win | 92.1019 |
| net_avg_loss | -107.9936 |
| avg_hold_time_bars | 44.3376 |
| exposure | 0.6240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
