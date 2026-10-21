# EMA Hourly Continuation — ORBS/USDT P34_55

**Symbol:** ORBS/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.4729 |
| net_win_rate | 0.4010 |
| gross_profit_factor | 0.7587 |
| gross_win_rate | 0.4033 |
| sharpe_ratio | -5.4052 |
| sortino_ratio | -1.5850 |
| max_drawdown | 0.8493 |
| cagr | -0.5209 |
| net_avg_win | 44.9862 |
| net_avg_loss | -63.6727 |
| avg_hold_time_bars | 6.9905 |
| exposure | 0.1331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
