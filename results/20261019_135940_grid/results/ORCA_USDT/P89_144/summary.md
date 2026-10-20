# EMA Hourly Continuation — ORCA/USDT P89_144

**Symbol:** ORCA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.4460 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8111 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -5.0920 |
| sortino_ratio | -1.5464 |
| max_drawdown | 0.8641 |
| cagr | -0.5404 |
| net_avg_win | 33.0576 |
| net_avg_loss | -58.6724 |
| avg_hold_time_bars | 6.3150 |
| exposure | 0.1358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
