# EMA Hourly Continuation — AEVO/USDT P12_144

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.7037 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9457 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.4340 |
| sortino_ratio | -0.6751 |
| max_drawdown | 0.6123 |
| cagr | -0.2793 |
| net_avg_win | 69.9025 |
| net_avg_loss | -91.6627 |
| avg_hold_time_bars | 39.9623 |
| exposure | 0.7197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
