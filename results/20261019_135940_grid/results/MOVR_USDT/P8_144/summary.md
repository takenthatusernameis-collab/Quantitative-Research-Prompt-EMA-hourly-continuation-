# EMA Hourly Continuation — MOVR/USDT P8_144

**Symbol:** MOVR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.5859 |
| net_win_rate | 0.4579 |
| gross_profit_factor | 0.8608 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -3.7124 |
| sortino_ratio | -1.1972 |
| max_drawdown | 0.7807 |
| cagr | -0.4419 |
| net_avg_win | 44.3972 |
| net_avg_loss | -64.0206 |
| avg_hold_time_bars | 30.3421 |
| exposure | 0.7379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
