# EMA Hourly Continuation — BABYDOGE/USDT P12_200

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 71 |
| net_profit_factor | 1.2044 |
| net_win_rate | 0.5634 |
| gross_profit_factor | 1.2686 |
| gross_win_rate | 0.5634 |
| sharpe_ratio | 0.5346 |
| sortino_ratio | 0.0658 |
| max_drawdown | 0.0819 |
| cagr | 0.0273 |
| net_avg_win | 103.4549 |
| net_avg_loss | -110.8369 |
| avg_hold_time_bars | 103.0704 |
| exposure | 0.3311 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
