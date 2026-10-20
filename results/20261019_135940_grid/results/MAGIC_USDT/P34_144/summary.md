# EMA Hourly Continuation — MAGIC/USDT P34_144

**Symbol:** MAGIC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6219 |
| net_win_rate | 0.4579 |
| gross_profit_factor | 0.8707 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -3.1685 |
| sortino_ratio | -0.9254 |
| max_drawdown | 0.6821 |
| cagr | -0.3540 |
| net_avg_win | 55.9190 |
| net_avg_loss | -75.9590 |
| avg_hold_time_bars | 23.3972 |
| exposure | 0.4552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
