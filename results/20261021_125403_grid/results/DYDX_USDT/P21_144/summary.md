# EMA Hourly Continuation — DYDX/USDT P21_144

**Symbol:** DYDX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.8952 |
| net_win_rate | 0.5158 |
| gross_profit_factor | 1.0555 |
| gross_win_rate | 0.5158 |
| sharpe_ratio | -0.6241 |
| sortino_ratio | -0.1673 |
| max_drawdown | 0.2756 |
| cagr | -0.0773 |
| net_avg_win | 86.7419 |
| net_avg_loss | -103.2062 |
| avg_hold_time_bars | 35.2206 |
| exposure | 0.5587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
