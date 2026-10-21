# EMA Hourly Continuation — DEEP/USDT P20_21

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 103 |
| net_profit_factor | 1.1866 |
| net_win_rate | 0.6214 |
| gross_profit_factor | 1.6132 |
| gross_win_rate | 0.6214 |
| sharpe_ratio | 0.6697 |
| sortino_ratio | 0.1125 |
| max_drawdown | 0.0807 |
| cagr | 0.0461 |
| net_avg_win | 94.5213 |
| net_avg_loss | -130.7197 |
| avg_hold_time_bars | 4.7282 |
| exposure | 0.0276 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
