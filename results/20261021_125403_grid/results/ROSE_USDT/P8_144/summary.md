# EMA Hourly Continuation — ROSE/USDT P8_144

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 1.0811 |
| net_win_rate | 0.5614 |
| gross_profit_factor | 1.2588 |
| gross_win_rate | 0.5614 |
| sharpe_ratio | 0.5252 |
| sortino_ratio | 0.1414 |
| max_drawdown | 0.1598 |
| cagr | 0.0558 |
| net_avg_win | 101.3973 |
| net_avg_loss | -120.0475 |
| avg_hold_time_bars | 50.2135 |
| exposure | 0.7806 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
